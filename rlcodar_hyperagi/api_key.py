"""
RLCoDAR-HyperAGI: API Key Manager

Generates and validates API keys for users.
One master key for now - can be extended to per-user keys later.
"""

import secrets
import hashlib
import json
import os
from datetime import datetime, timedelta
from typing import Optional, Dict

# Master API key (generated once, stored in env)
MASTER_API_KEY = os.getenv("RLCODAR_API_KEY", None)

# Key storage (in production, use database)
API_KEYS_DB = "api_keys.json"


def generate_api_key(user_id: str = "master") -> str:
    """Generate a new API key"""
    key = f"rlcodar-{secrets.token_hex(32)}"
    
    # Store key metadata
    key_data = {
        "key": hashlib.sha256(key.encode()).hexdigest(),
        "user_id": user_id,
        "created": datetime.now().isoformat(),
        "expires": (datetime.now() + timedelta(days=365)).isoformat(),
        "usage_count": 0,
        "last_used": None
    }
    
    # Save to database
    save_key(key_data)
    
    return key


def validate_api_key(key: str) -> bool:
    """Validate an API key"""
    if not key:
        return False
    
    key_hash = hashlib.sha256(key.encode()).hexdigest()
    
    try:
        with open(API_KEYS_DB, 'r') as f:
            keys = json.load(f)
        
        for stored_key in keys:
            if stored_key["key"] == key_hash:
                # Check expiration
                expires = datetime.fromisoformat(stored_key["expires"])
                if datetime.now() > expires:
                    return False
                
                # Update usage
                stored_key["usage_count"] += 1
                stored_key["last_used"] = datetime.now().isoformat()
                save_keys(keys)
                
                return True
        
        return False
    except FileNotFoundError:
        return False


def save_key(key_data: Dict):
    """Save a single key"""
    try:
        with open(API_KEYS_DB, 'r') as f:
            keys = json.load(f)
    except FileNotFoundError:
        keys = []
    
    keys.append(key_data)
    save_keys(keys)


def save_keys(keys: list):
    """Save all keys"""
    with open(API_KEYS_DB, 'w') as f:
        json.dump(keys, f, indent=2)


def get_master_key() -> str:
    """Get or create master API key"""
    global MASTER_API_KEY
    
    if MASTER_API_KEY:
        return MASTER_API_KEY
    
    # Try to load from database
    try:
        with open(API_KEYS_DB, 'r') as f:
            keys = json.load(f)
        
        # Find master key
        for key_data in keys:
            if key_data["user_id"] == "master":
                # Key exists but we don't have the actual key value
                # Generate new one
                break
    except FileNotFoundError:
        pass
    
    # Generate new master key
    MASTER_API_KEY = generate_api_key("master")
    
    return MASTER_API_KEY


if __name__ == "__main__":
    # Generate and display master key
    master_key = get_master_key()
    
    print("=" * 60)
    print("RLCoDAR-HyperAGI API Key")
    print("=" * 60)
    print(f"\nMaster API Key: {master_key}\n")
    print("Save this key and set it in your environment:")
    print(f"  export RLCODAR_API_KEY={master_key}")
    print("\nOr add to .env file:")
    print(f"  RLCODAR_API_KEY={master_key}")
    print("=" * 60)

BAPXDI DATASET REGISTRY
Verified on HuggingFace. Public. Parquet. HTTP Range only. No training.

WIKIPEDIA ALL LANGUAGES
The wikimedia wikipedia dataset contains cleaned articles from all languages.
Available languages include English Arabic Chinese Hindi Spanish French German Japanese Korean Russian Portuguese Tamil Swahili Yoruba and three hundred more.
Each article has a title text and url field. License is Creative Commons Attribution ShareAlike.
The English Wikipedia alone has over forty one parquet shards with millions of articles.
This is the largest open multilingual knowledge base ever assembled by humans.

WIKTIONARY AND WIKISOURCE
The wikimedia wikisource dataset contains primary texts from seventy five languages.
Includes books laws historical documents and literary works in their original languages.
Useful for etymology definitions and primary source reasoning across cultures.

MATHEMATICS CHAIN OF THOUGHT
The NuminaMath dataset from the AI Mathematical Olympiad team contains eight hundred sixty thousand math problems.
Every solution is written as a full chain of thought reasoning trace showing every step.
Sources range from Chinese high school exercises to American and international olympiad competition problems.
Each row has a problem field a solution field and a source field. License is Apache.
This dataset teaches the diffusion kernel how mathematical reasoning works step by step.

The open web math dataset contains fourteen point seven billion tokens of mathematical text from the internet.
Filtered from two hundred billion HTML files on CommonCrawl down to six million documents.
Covers formulas proofs calculations algebra calculus statistics and applied mathematics.

The proof pile two dataset from EleutherAI contains one hundred billion tokens of mathematical text.
Sources include the algebraic stack ArXiv papers and OpenWebMath formal proofs and theorems.

The MetaMath dataset contains three hundred ninety five thousand math question answer pairs augmented from GSM8K and MATH benchmarks. License is MIT.

The Orca Math dataset from Microsoft contains two hundred thousand grade school math word problems with verified answers. License is MIT.

CODE ALL PROGRAMMING LANGUAGES
The Stack version two from BigCode contains code across six hundred programming languages.
Covers Python JavaScript TypeScript Rust Go Java C and hundreds more programming languages.
This is the largest open source code corpus available to researchers.

The CodeFeedback dataset contains filtered code instruction pairs with query answer and difficulty ratings. License is Apache. Covers algorithmic problems system design debugging and code generation.

The OpenCoder dataset stage two contains one hundred thousand code supervised fine tuning pairs with execution validated responses. License is MIT.

The DeepMind code contests dataset contains ten thousand competitive programming problems from Codeforces AtCoder CodeChef LeetCode and HackerEarth. Each problem has description solutions and test cases. This is the AlphaCode training dataset made public. License is Creative Commons.

WEB SEARCH AND GENERAL KNOWLEDGE
The FineWeb dataset from HuggingFace contains eighteen point five trillion tokens of cleaned web data.
Built from ninety six CommonCrawl snapshots from two thousand thirteen to two thousand twenty four.
This is the largest open source web dataset ever released covering the entire public internet.
Each row has text url date language and quality score fields. License is Open Data Commons.
Eighteen trillion tokens of human knowledge available via HTTP Range requests with no training required.

The WikiText dataset from Salesforce contains one hundred million tokens from Wikipedia Good and Featured articles chosen by human editors for quality. License is Creative Commons.

REASONING AND THINKING
The OpenHermes dataset from Teknium contains one million instruction conversation pairs covering reasoning philosophy science coding math and creative tasks. This dataset underpins several top open source reasoning models.

The WildChat dataset from Allen AI contains one million real human conversations with ChatGPT across many languages and reasoning styles. Real human reasoning patterns captured in natural multilingual conversation.

The GSM Hard dataset from Reasoning Machines contains hard math word problems testing multi step numerical reasoning. License is MIT.

MULTILINGUAL ALL LANGUAGES INSTRUCTION
The Aya dataset from Cohere Labs contains two hundred four thousand human annotated instruction pairs covering sixty five languages including Tamil Hindi Swahili Yoruba Urdu Bengali and all major world languages.
Annotated by native speakers from around the world. License is Apache.
This enables bapXdi to reason and generate in any human language without separate multilingual models.

HOW BAPXDI READS THESE
Language layer decides which dataset contains relevant knowledge for the query.
HTTP Range request fetches four thousand bytes from the Parquet shard.
Mercury diffusion crystallizes toward those bytes in twelve steps using the formula b equals b plus target divided by two.
Query window selection finds the most relevant passage in the fetched bytes.
Output is the document content that answers the query. No hallucination possible.
RAM clears after every query. Nothing stored. Device stays clean.
No training. No weights. No coordinates. No storage.
The bytes are already the intelligence. The electrons already speak the language.

HOW BAPXDI READS WIKIPEDIA:
Wikipedia is already on HuggingFace as wikimedia wikipedia dataset.
The English Wikipedia has forty-one Parquet shards.
Each shard contains millions of articles with title text and url fields.
bapXdi sends an HTTP Range request to the Parquet file URL.
The Parquet footer is read first — only eight bytes plus footer length.
Footer contains byte offsets of all row groups in the file.
Query words select which row group to fetch.
That row group contains real Wikipedia article text.
Mercury diffusion runs over those bytes.
Answer crystallizes from the Wikipedia bytes that match the query.
No download. No storage. No training on Wikipedia.
Wikipedia stays on HuggingFace servers. bapXdi just reads the relevant bytes.

FINEWEB-2 — MULTILINGUAL WEB
HuggingFaceFW/fineweb-2 — ODC-BY — 1000+ languages
The FineWeb-2 dataset is a multilingual update to FineWeb bringing high quality pretraining data to over one thousand languages.
Fully reproducible, ODC-By license, validated through hundreds of ablation experiments.
HTTP Range: https://huggingface.co/datasets/HuggingFaceFW/fineweb-2/resolve/main/data/eng_Latn/train-00000-of-01472.parquet

COSMOPEDIA v2 — SYNTHETIC EDUCATIONAL
HuggingFaceTB/smollm-corpus — ODC-BY
Cosmopedia v2 contains over thirty-nine million synthetic textbooks, blog posts, and stories.
Largest synthetic dataset for pre-training. High quality educational content across all subjects.
HTTP Range: https://huggingface.co/datasets/HuggingFaceTB/smollm-corpus/resolve/main/cosmopedia-v2/train-00000-of-00104.parquet

HOTPOTQA — MULTI-HOP REASONING
hotpotqa/hotpot_qa — CC-BY-SA-4.0
113K Wikipedia-based question-answer pairs requiring multi-hop reasoning across documents.
Questions require finding and reasoning over multiple supporting documents to answer.
Sentence-level supporting facts for reasoning. Diverse questions not constrained to knowledge schemas.
This is exactly what RLM recursive hops implement — multi-hop reasoning across docs.
HTTP Range: https://huggingface.co/datasets/hotpotqa/hotpot_qa/resolve/main/data/train-00000-of-00001.parquet

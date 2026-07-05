# Task 2: Agentic AI / Workflow AI Understanding

## Agentic AI:
Agentic AI is one of the sub fields in Artificial Intelligence. It is an advanced form of AI, which is focused around autonomous decision making and taking actions. Unlike tradional AI, which primarily respond to commands, given tasks or analyzes given data. An Agentic AI can set goals, plan for the goals and then finally takes actions upon it, to execute the task with minimal human intervention. It is an emerging technology in the domain of AI.


## Workflow AI:
Workflow AI or AI Workflow is a process in which structured, automated sequence of tasks, where an AI basically LLM is responsible for the coordination of steps, it executions and procedures. Wokrflow AI can understand the context, gain insights and patters from the data and be dynamic in nature or adapt to changing requirements and inputs unlike tradionational AI.


## AI Copilots/Assistanst:
An AI Copilot is a type of integrated digital assistant that is power by an AI(mostly LLMs) which has the capability to help us in our day to day tasks. It is mostly used in coding, where it can take a look at the project repo and it's contents. However it can and it often gives us suggestions from external sources like articles, documentations, web pages and etc. 
Some of the examples of AI Copilots are GithubCopilot, Microsoft Copilot and etc


## Differnece between standalone AI model and AI Integrated into a product workflow:
A simple standalone AI model can only generate prediction for the things it was trained for. For example an CNN model which is widely used in Computer Vision related applications and area. Suppose it was built and trained on Cats or Dogs images dataset. Now it can simply be used to detect if the given image is that of a Dog or Cat. But when integrated into a workflow it can be used in several ways such as detection of Animals(Cats and Dogs) during driving, or detecting their particular breed.

Another example related to LLM that I would like to give is that. Suppose there is a particular kind of LLM whichtakes in messages in simple terms/english written by humans and gives us the SQL queries which is further used to retrieve the data from the database. This is based off on one of the real life examples. Swiggy the popular food delivery company uses this technique into their workflow whenever a customer is chatting through their chatbot and has such queries which requires data or information retrieval from the database itself. Swiggy had built and trained their text-to-SQL LLM model from scratch completley inhouse.


## My Past Experiences with GenAI, LLMs, RAGs, AI Agent, Workflow Automation and etc.:

My time as an intern at Ebizon Cloud was spent building a complete Retrieval-Augmented Generation (RAG) system to handle technical inquiries on Oracle Cloud Infrastructure documentation. I put in place FAISS as the vector store, relying on OpenAI embeddings for retrieval, and ran benchmarks on a host of large language models such as GPT, Gemini, Mistral, Nemotron and DeepSeek V3 to see which would deliver the most accurate and well-grounded results. To keep the system from straying from the source material, I applied hallucination mitigation via confidence scoring and citation-based generation, all while doing the necessary prompt engineering and tuning on a set of curated questions.

Over at Arcitech AI, I put together an automated pipeline for audio analytics. It is an asynchronous FastAPI microservice that takes customer call recordings and runs them through the gauntlet: ingestion, transcription, PII redaction, NER, emotion recognition, KPIs and summarization before handing off the data via REST API. By making this a production-ready workflow, we were able to do away with manual analysis and scale our operations.

I have found my strength lies in putting AI into production software as well as to creating standalone models. Creating and training models from the ground up has enabled me to understand things from first principle perspective which I found to be very cruicial in the domain AI. Working with the backend team at Arcitech, I integrated AI modules into the core product so the application could make use of REST endpoints for everything from transcription to sentiment analysis. In much the same way at Ebizon, I rolled out an internal knowledge assistant for OCI that gave users a web front end to get answers with full transparency and links back to the original docs. Such work has given me a good sense of how to build AI systems that are not just research exercises but are reliable and fit for purpose in a real-world environment.




# Task 3: AI Use Case Evaluation

(1) Surrogate ML Models for Faster Prediction:

What it solves: Full physics simulations or even just the script behind this heat sink model from this assessment are too slow to be run on the fly for rapid design exploration, or to provide real-time feedback during design iterations. A trained surrogate model can provide a prediction in milliseconds, rather than having to run the underlying calculation/simulation every time.

What data would be required: The dataset used to train the model would need to be generated from the underlying physics model (or from prior simulation/experimental results, if available) by exploring the input space that the model is supposed to cover – precisely the task that was accomplished with the script in task 1 of the assessment. To ensure the ability to extrapolate, the model should be trained on the widest possible range of realistic operating conditions.

ML, GenAI, workflow AI, or combination: Mostly ML(regression) random forest, gradient boosting, or a neural network, possibly with a GenAI component on top to provide human-readable explanations of its predictions.

How to validate it works correctly: By holding out a test set and evaluating the model’s performance on it, using metrics such as MAE, RMSE, or R2 compared to the physics model, as was done in task 1. Additionally, a few independent test simulations not used in training could be performed, and the model’s performance on them evaluated. In production, if the model’s confidence estimates or prediction error start to increase significantly, it might be necessary to retrain it on new data if, for example, the design space starts including operating conditions not present in the training data.


(2) Knowledge retrieval from engineering documents (RAG)
Problem to Solve: Engineering teams often have extensive corpuses of reference documents (datasheets, previous design documentation, internal standards, past assessment reports, etc.) which are difficult to query effectively with standard search techniques due to inconsistent phrasing of concepts across different documents. An engineer may know that some information exists “somewhere in the documents,” but not be able to find it quickly.

Data Needs: The relevant corpuse of internal documents (PDFs, reports, datasheets, calculations, etc.) that need to be searchable, in a form amenable to passage retrieval (vector database or similar), plus document metadata such as version control.
ML, GenAI, Workflow AI, or Combo: Combination. The question-answering would use retrieval augmented with a GenAI model to synthesize the answer from the retrieved passages with proper citations. The retrieval itself could be done with standard ML methods (embedding vectors) or with a GenAI model fine-tuned for passage retrieval.

Validation: Requires a set of test questions with known answers and corresponding documents. For each test question, both retrieval effectiveness (did the right document come up?) and answer faithfulness (does the answer actually use the retrieved documents, not make up information?) should be validated. Because hallucination is a known weakness of GenAI models, any answer produced by this system should ideally be traceable to specific cited documents that a human could review.


(3) AI-Assisted Input Validation & Missing Parameter Detection
What problem it solves: Engineering calculation tools often fail silently or give nonsensical results when a user inputs an invalid value, uses inconsistent units, or forgets to fill in required parameters (e.g. entering TIM conductivity in the wrong units, or leaving an air velocity field blank and having a script fill it with zeroes). Being able to catch that before running a computation saves wasted simulation time and misleading design reviews.

What data would be required: Historic records of valid input ranges (for example, what TDP, velocity, or conductivity values are plausible for the hardware under consideration), and if available, examples of invalid inputs and their corrections, to train pattern recognition models.

ML, GenAI, workflow AI, or combination: Mainly workflow-assisted AI for range checks, required field checks, and unit validation with some degree of ML or GenAI to catch "these inputs are suspicious given comparable past runs" to account for human error.
How to validate it works correctly: Have a set of known bad inputs that should raise alerts, and validate that they do. Have a set of known good inputs that shouldn't raise any alerts, and ensure that they don't. The false-positive rate in real-world use is also a good metric to track, as engineers will likely stop using an overly-pesky validation system.




# Task 4: 

## Why do you want to join Expert Thermal / XThermal?
I am an Aspiring ML engineer who's spent real time on physics-adjacent and signal-heavy problems (audio analytics pipelines, CNN models) rather than pure software or webbased ML, this role is a combination of thermal engineering + AI surrogate modeling and definitely a lot more than that, it sits right at that intersection of Physics and AI(including maths and computer science). I find it to be a really exiciting and wholesome opportunity. Not only I will be tested at each and every step while working at Expert Therman / XThermal. But I will need to evolve or transform myself just like energy in physics. I will need to transform from one form to the other. Or speaking in  other relatable manner keep on getting excited from one state to the other state just like atoms and energy in the universe....

## What are you most interested in building in AI/ML?
Just like how Physics is the study and observation of nature, and based off on it humanity has progressed so far and given birth to so many kinds of Engineering Marvels. I too man very interested in the aspect of Research and Development in the field of AI/ML. I may be an aspiring Engineer and the role is that of one too. But have to heart and soul of an Scientist just like a Physics Expert. Learning and interpreating things from ground up. Understand a problem, it's concept and engineer it solution from first principle thinking. In those process finding out and improving newer things or even on the granular level is what excites me about this role.

## Are you more interested in ML models, GenAI workflows, physics-aware AI, or product AI integration?
I am more interested in the ML Models, especially it requireing physics-aware AI and then on further integrating it into GenAI Workflows or Product AI Integration as per the needs and requirements.

## How do you handle ambiguous problems where requirements are not fully defined?
I would handle ambiguous problems by firstly understanding the nature and core of the problem. Especially since in AI/ML problems are often based on certain domains. For example one could be building a trading bot, instead of brute forcing their way into making a model. It's far more practical and sensible to first get to know little bit about trading, stock-share market and then do the problem solving and modelling. So, just like that I would find ways and do Research and Development in case of amiguous problems with no proper defined requirements 

## Are you comfortable working in a fast-moving startup environment?
Yes I am absolutley  comfortable working in a fast paced startup enviroment. Just like how I am a fresher and I am yet to learn and grow a lot, I am commited and totally comfortable growing and working in such fast paced startup enviroment.

## How do you think you can grow within our team?
I would grow withing our team, as I am now incomplete and I have a long way to go in my career. I know that these kinds of enviroments require a person to thrive, face challenges and hurldes rather than being in the same loop or being static. That is how I intend to grow as well as grow withing the team while bringing my best to the table from problem to problem and time to time.

## This role calls for ownership, commitment, and initiative. How would you bring new ideas,create solutions, and take on greater responsibility over time?
I believe in taking ownership, commitment, and initiative especially before being explicitly instructed. As in order to grow and evolve I have to break the barrier and aim for more than I have till now. I would give me best in doing Research but even more being grounded and aware of the problem given first than directly getting into work. Also exploring all possble scenarios and proving myself and my capabilites and expanding my horizion. I understand this role at the startup requires one to wear various Hats than just traditional roles at MNCs. One has to be like a unit or a army.
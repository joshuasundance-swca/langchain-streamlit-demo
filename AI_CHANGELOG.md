# AI CHANGELOG
## [Added Azure OpenAI Embeddings option to app](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/c60388636d63567bd9bfe4b7bbfebf734d3100da)
Fri Oct 6 18:35:40 2023 -0400
- This commit introduces the option to use Azure OpenAI for embeddings in the langchain-streamlit-demo app. It adds the necessary environment variables and updates the code to handle the new option. The changes include:
- 1. Addition of the AZURE_OPENAI_EMB_DEPLOYMENT_NAME environment variable in the Kubernetes resources.
- 2. Update of the app.py file to handle the Azure OpenAI option. If Azure embeddings are available, a toggle is displayed to the user to switch between Azure and OpenAI directly.
- 3. Update of the get_texts_and_retriever function in llm_resources.py to accept additional arguments for azure_kwargs and use_azure.
- 4. Update of the defaults.py file to include the AZURE_OPENAI_EMB_DEPLOYMENT_NAME in the list of Azure environment variables.
## [Refactored code to improve readability and maintainability](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/0ce4fb3a9cb43ee563729df1d6b682511e17248f)
Fri Oct 6 18:15:24 2023 -0400
- 1. Updated kubernetes resource configuration to add environment variables for SHOW_LANGCHAIN_OPTIONS and SHOW_AZURE_OPTIONS.
- 2. Refactored the app.py script to import default values from a single source, improving readability and maintainability of the code.
- 3. Updated defaults.py to define a namedtuple for default values, which is imported in other scripts.
- 4. Modified llm_resources.py to accommodate changes in the import of default values.
## [Refactor code by moving logic to a separate module](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/21eccfc51cf90268826929cddbf2bfa42bc2f5eb)
Fri Oct 6 16:26:26 2023 -0400
- The commit moves a significant amount of logic from 'app.py' to a new module named 'llm_resources.py'. This includes the methods for getting the runnable instance, the language model, and the texts and retriever. The aim of this refactoring is to improve code organization, readability, and maintainability.
## [Refactored code and improved project structure](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/87d698488900d63b992059b6f291d6981773fb4b)
Fri Oct 6 15:59:43 2023 -0400
- Moved model constants and environment variables into a separate 'defaults.py' file for better code organization and readability.
- Updated 'app.py' to import these constants and variables from the new 'defaults.py' file.
- Modified '.idea/langchain-streamlit-demo.iml' to include a new source folder, improving the project's structure.
## [Added Azure OpenAI environment variables to Kubernetes deployment](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/f39ac3b55d8e57db36ff4a43a4b95dda1fa46e9d)
Fri Oct 6 14:15:57 2023 -0400
- In the Kubernetes resource configuration file, several environment variables related to Azure OpenAI have been added. These include the base URL, API version, deployment name, API key, and model version. The values for these variables are fetched from the 'langchain-streamlit-demo-secret' secret.
## [Bumped version from 0.0.12 to 0.0.13](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/d767997980a751389dcbec81b1bcaa1c10267534)
Fri Oct 6 14:03:44 2023 -0400
- Updated the current_version in bumpver.toml from 0.0.12 to 0.0.13.
- Updated the image tag in the Kubernetes resources.yaml file to use the new version 0.0.13.
- Updated the __version__ variable in the app.py file to reflect the new version 0.0.13.
## [Refactored application code and updated dependencies](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/979e3bd9fe449bea04e5ceda5c1a72be2e824c58)
Fri Oct 6 13:58:33 2023 -0400
- Refactored the application code in 'langchain-streamlit-demo/app.py' to improve clarity and organization. Changes include renaming 'AZURE' to 'Azure OpenAI' in the 'MODEL_DICT' and modifying related conditional checks, renaming 'Advanced Options' to 'Advanced Settings', and restructuring 'LangSmith Options' into its own section within the sidebar.
- Updated the 'streamlit' version from '1.27.1' to '1.27.2' in 'requirements.txt'.
## [Added support for Azure Chat models in the Streamlit application](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/72c3d8c60b3e15ce8d89f926ffe2ab845d3d9c1b)
Fri Oct 6 13:50:43 2023 -0400
- The commit introduces Azure Chat models into the Streamlit application. It includes the addition of the AzureChatOpenAI model in the import statement and the MODEL_DICT. Environment variables for Azure are also defined and retrieved from the system environment. User interface elements for Azure options have been added within an expandable section in the sidebar. Finally, an instance of AzureChatOpenAI is created if all Azure details are available and the selected provider is Azure.
## [Updated langsmith package](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/e4b72fedeb71c822b6a76ed84199fef2bbc3bf8a)
Fri Oct 6 13:02:43 2023 -0400
- The langsmith package version was updated from 0.0.41 to 0.0.43 in the requirements.txt file.
## [Updated langchain version in requirements.txt](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/2c41972749e5524bba738b37e6d31416e657fec6)
Thu Oct 5 13:54:14 2023 +0000
- The langchain package version in requirements.txt has been upgraded from 0.0.305 to 0.0.308. This update may include bug fixes, feature enhancements or performance improvements.
## [Updated application version to 0.0.12](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/2bee8f19e2fa71c333588a3531b55fe062701328)
Mon Oct 2 09:13:48 2023 -0400
- The application version has been updated from 0.0.11 to 0.0.12 in three different files. These include bumpver.toml, resources.yaml under kubernetes, and app.py under langchain-streamlit-demo. In bumpver.toml, the current_version value is updated. In resources.yaml, the image version for the container 'langchain-streamlit-demo' is updated. In app.py, the __version__ variable is updated to reflect the new version.
## [Updated dependencies in requirements.txt](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/9747a2d97d4e60861e6d0cc8de7ca8076a6ac971)
Mon Oct 2 09:10:05 2023 -0400
- The langchain and langsmith dependencies have been updated to versions 0.0.305 and 0.0.41 respectively.
- The openai dependency has been updated to version 0.28.1.
- The previous comment about rolling back the langchain update to avoid a bug has been removed, implying the bug has been fixed in the new version.
## [Version Bump from 0.0.10 to 0.0.11](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/58978f749bdf319a2c2f76e74a46e7d905b7bf69)
Sat Sep 30 01:31:32 2023 -0400
- Updated the current_version in bumpver.toml from 0.0.10 to 0.0.11.
- In the Kubernetes resources.yaml, updated the image version of langchain-streamlit-demo from 0.0.10 to 0.0.11.
- In the langchain-streamlit-demo/app.py, updated the __version__ from 0.0.10 to 0.0.11.
## [Updated README.md with minor content and structure changes](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/241c14d23e150e0be6edee2c28e32c1b4a519c73)
Sat Sep 30 01:29:08 2023 -0400
- This commit includes changes to the README.md file. The authorship of the README has been clarified to indicate that it was originally written by Claude 2. The Features section has been updated to include a new model from Anyscale Endpoints, and to mention the addition of various forms of document chat. The Code Overview section was removed. A minor formatting change was made to the Docker run command. The Docker Compose instructions were simplified by removing a redundant command.
## [Improved UI labels and refactored code in langchain-streamlit-demo](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/f8e912146cbca42cbd456abb123b5223b0924c45)
Sat Sep 30 01:24:47 2023 -0400
- This commit includes changes to improve the user interface labels for better readability. The labels 'chunk_size' and 'chunk_overlap' have been changed to 'Number of Tokens per Chunk' and 'Chunk Overlap' respectively.
- Additionally, the code for handling the full response and the initialization of the `st.session_state.chain` has been refactored for better readability and maintainability. The code now clearly distinguishes between the cases when `use_document_chat` is true or false, and the initialization of `st.session_state.chain` is more streamlined.
## [Refactored chat functionality and removed unnecessary code in app.py and qagen.py](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/923e6fac55336c07c8af10b74742b117517bd757)
Sat Sep 30 01:10:43 2023 -0400
- In app.py, removed the StreamlitCallbackHandler import and simplified the logic for handling chat inputs. Removed the document chat condition in the if statement, and directly implemented the regular chat functionality. Simplified the condition for using document chat, and refactored the way rag_runnable is retrieved based on the document chat chain type.
- In qagen.py, removed the unnecessary import of reduce from functools and the combine_qa_pair_lists function. Simplified the get_rag_qa_gen_chain function by directly converting the parsed_output to a string.
## [Refactored code for readability and efficiency](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/bfaa0c3cf1792d9cb5086657f9ded983ba616662)
Fri Sep 29 23:12:56 2023 -0400
- This commit includes changes in the 'app.py' and 'qagen.py' files. In 'app.py', the code has been refactored to improve readability and efficiency. The configuration dictionary has been moved outside the if-conditions to avoid redundancy. Also, the condition checking for 'Summarization' and 'Q&A Generation' has been combined to reduce nested if-statements.
- In the 'qagen.py' file, two new methods 'to_str' have been added to the 'QuestionAnswerPair' and 'QuestionAnswerPairList' classes. These methods convert the question and answer pairs into a string format. This change has moved the responsibility of string formatting from 'app.py' to 'qagen.py', making the code more modular and easier to maintain.
## [Updated summarization functionality in Streamlit app](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/dd9bfbddff559ce0065c236ccc6419f987a61664)
Fri Sep 29 22:43:24 2023 -0400
- Replaced the existing get_summarization_chain function with get_rag_summarization_chain in the Streamlit app.
- The get_rag_summarization_chain function now takes in the prompt, retriever and the language model as parameters.
- Refactored the way the summarization chain is invoked and the full response is generated.
- Updated the get_rag_summarization_chain function in the summarize module to return a RunnableSequence.
## [Updated model_name parameter in ChatOpenAI instantiation](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/06099804b5d0a4d635beb8a0021ac84b22cb0529)
Fri Sep 29 18:38:23 2023 -0400
- Replaced hardcoded 'test' value for model_name parameter with a variable named 'model'. This change allows the model name to be dynamically set when the ChatOpenAI class is instantiated.
## [Refactored model instantiation and removed deprecated functions](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/c2ef57040f3231cc3fa80157d93d0d8420f21351)
Fri Sep 29 18:38:01 2023 -0400
- Updated the instantiation of ChatOpenAI, ChatAnthropic, and ChatAnyscale classes by swapping the model and model_name parameters to match their class definitions.
- Removed the commented out get_qa_gen_chain function in qagen.py.
- Removed commented out code related to raw_results and results in app.py, simplifying the logic.
## [Refactored the data processing pipeline](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/8106321374be538f2740587a9a3d68e9cb82310f)
Fri Sep 29 18:31:46 2023 -0400
- Removed the 'combine_qa_pair_lists' function from the data processing pipeline in 'app.py'.
- Directly accessed 'QuestionAnswerPairs' from 'raw_results' instead of using 'combine_qa_pair_lists' function.
- Commented out the print statement for 'raw_results'.
## [Refactored code to change 'input' to 'context' in langchain-streamlit-demo](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/3550ebd119e342869167a228929538c069350942)
Fri Sep 29 18:19:58 2023 -0400
- This commit includes a change in the variable name from 'input' to 'context' in both app.py and qagen.py files. The change was made in the section where the document page content is being processed. This change is likely aimed at improving code readability and consistency.
## [Added customizability for number of chunks in retriever](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/457889e5dc68143a1a5f935ca6af849bd380666c)
Fri Sep 29 18:16:51 2023 -0400
- This commit introduces a slider in the UI allowing the user to select the number of chunks that will be used for context in the retriever. The 'get_texts_and_retriever' function was updated to include a new parameter 'k' that defaults to the newly introduced constant 'DEFAULT_RETRIEVER_K'. This 'k' value is then used in the creation of both the 'bm25_retriever' and 'faiss_retriever'.
## [Updated Q&A Generation method and invocation](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/8aab446c1cbafbdb04dcf6d56ed77413f1e63f65)
Fri Sep 29 18:13:30 2023 -0400
- Replaced the get_qa_gen_chain method with get_rag_qa_gen_chain in app.py and qagen.py. This change updates the Q&A Generation method used in the Document Chat feature.
- Changed the way the Q&A Generation method is invoked. Instead of using the batch method, we now use the invoke method. This change is expected to improve the efficiency of the Document Chat feature.
## [Implemented RAG-based Q&A Generation Chain](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/6467ea59cd8b5eb4859d20c8f84152402833cb92)
Fri Sep 29 18:04:08 2023 -0400
- Added a new function 'get_rag_qa_gen_chain' in 'qagen.py' to set up a RAG-based Q&A generation chain using a retriever and a language model.
- Adjusted the 'app.py' to include a commented-out option to use the new RAG-based Q&A generation chain.
## [Bump version from 0.0.9 to 0.0.10](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/bb29f017b57cd891d1f9ae86e212ec6c92b5aa43)
Fri Sep 29 13:17:34 2023 -0400
- Updated the version number in the bumpver.toml, kubernetes/resources.yaml, and langchain-streamlit-demo/app.py files. The new version is 0.0.10.
## [Updated retriever logic and removed question validation](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/930d4126fe97dbb403fa498b5322e10815d06179)
Fri Sep 29 11:17:45 2023 -0400
- In the 'langchain-streamlit-demo/app.py' file, the logic to retrieve texts has been updated. The FAISS retriever has been replaced with an ensemble retriever that uses both the BM25 and FAISS retrievers. The BM25 retriever's 'k' parameter has been set to 4, and the FAISS retriever has been updated to use a vector store.
- In the 'langchain-streamlit-demo/qagen.py' file, the field validator for the 'question' field in the 'QuestionAnswerPair' class has been removed. This means that questions no longer need to end with a question mark to be valid.
- The 'requirements.txt' file has been updated to include the 'rank_bm25==0.2.2' package, and the 'streamlit' package has been updated to version '1.27.1'.
## [Updated the refine_template in summarize.py](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/736288ed897a6bf1b5c0be7c0481011598351395)
Thu Sep 28 20:55:25 2023 -0400
- The refine_template string in the summarize.py file has been updated. A newline character has been added after the 'User input: {query}' part of the string for better readability.
## [Updated application version to 0.0.9](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/40604bea7723c4c05b4c36289950e6d8a25b7690)
Thu Sep 28 20:41:33 2023 -0400
- The version number in the bumpver.toml file has been updated from 0.0.8 to 0.0.9.
- The Docker image version for the langchain-streamlit-demo app in the Kubernetes resources.yaml file has been updated from 0.0.8 to 0.0.9.
- The __version__ variable in the app.py file of the langchain-streamlit-demo app has been updated from 0.0.8 to 0.0.9.
## [Improved text formatting in Q&A response](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/4eaf9de17247ed7e6bdc1771ff31639cca9e903d)
Thu Sep 28 20:39:28 2023 -0400
- This commit adjusts the formatting of the Q&A response in the langchain-streamlit-demo app. It adds an extra newline between the question and answer parts, and another newline between each Q&A pair for better readability.
## [Updated application version to 0.0.8](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/8c80fe821129d05b8b714beb56a4e0bbca6ce676)
Thu Sep 28 20:36:46 2023 -0400
- The application's version number has been updated from 0.0.7 to 0.0.8 in the following files: bumpver.toml, resources.yaml, and app.py.
- In bumpver.toml, the current_version field was updated to reflect the new version.
- In resources.yaml, the image tag for the langchain-streamlit-demo container was updated to use the new version.
- In app.py, the __version__ variable was updated to the new version.
## [Refactor variable names in Streamlit app](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/9bf9004ce3ba4160e1c33f57e0c5e48c0ff4f628)
Thu Sep 28 20:33:17 2023 -0400
- The variable 'output_text' was renamed to 'full_response' in the Streamlit application to better reflect its purpose. This change improves code readability and understanding.
## [Bumped version from 0.0.6 to 0.0.7](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/d41f4a4356709af4dbd81982fdefb0a6dba21ef6)
Thu Sep 28 19:56:12 2023 -0400
- Updated the version number in bumpver.toml, resources.yaml, and app.py.
- This commit includes changes to the version number in the bumpver configuration, the Docker image tag in the Kubernetes resources, and the version variable in the app.py file.
## [Added Summarization Feature to Streamlit App](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/47c2ffc283d1e1754c1f64ab5fb793694bc9f24f)
Thu Sep 28 19:53:59 2023 -0400
- This commit introduces a summarization feature to the Streamlit application. It does so by creating a new 'summarize.py' file and integrating it into the 'app.py' file.
- In 'app.py', the 'LLMChain' import has been moved and the 'get_summarization_chain' function has been imported from 'summarize.py'.
- A new option 'Summarization' has been added to the 'Document Chat Chain Type' dropdown menu.
- When 'Summarization' is selected from the dropdown, the 'get_summarization_chain' function is called to create a summarization chain.
- The summarization chain is then used to generate a summary of the document, which is displayed in the Streamlit app.
- In the 'summarize.py' file, a new summarization chain is defined using the 'load_summarize_chain' function from the 'langchain.chains.summarize' module. The chain uses two custom prompt templates for summarizing and refining the document text.
## [Enhanced document chat functionality in langchain-streamlit-demo](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/622ac6610de2f89368031d57ebd148259e5d7fcc)
Thu Sep 28 16:55:16 2023 -0400
- This commit includes enhancements to the document chat functionality in the langchain-streamlit-demo application. It introduces a new document chat chain type 'Q&A Generation' and updates the provider variable to be stored in the session state. The commit also adds a new file 'qagen.py' which contains code for generating question and answer pairs from a given text.
## [Bump version from 0.0.5 to 0.0.6](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/f431ca56717b9e704226c3448a552fe31c90d77d)
Thu Sep 28 14:42:31 2023 -0400
- The version number in the 'bumpver.toml', 'kubernetes/resources.yaml', and 'langchain-streamlit-demo/app.py' files has been updated from 0.0.5 to 0.0.6. This indicates a new iteration of the software with potential minor changes or bug fixes.
## [Updated ruff-pre-commit version](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/50b28c9ac810cf9ff1c58e0b98f4ca7dfe3f94f5)
Wed Sep 27 20:58:22 2023 -0400
- The ruff-pre-commit version in the pre-commit configuration file was updated from v0.0.290 to v0.0.291.
## [Updated file exclusions in pre-commit config](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/c8b46036933d50ca6befc5d4fa43bcb29f05c75a)
Wed Sep 27 20:57:54 2023 -0400
- The pre-commit configuration has been updated to exclude the AI_CHANGELOG.md file. Previously, the configuration was set to exclude .idea and docs directories. The repository and hook details remain unchanged.
## [Refactored chain_type_help in app.py and updated AI_CHANGELOG.md](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/a1b0a6fd0b22021079e741929eb7671855192cb0)
Wed Sep 27 20:56:47 2023 -0400
- In app.py, the chain_type_help dictionary was refactored to directly generate a string with the help links for each chain_type_name, removing the need for a separate dictionary.
- In AI_CHANGELOG.md, a newline was added at the end of the file and entries were made for the addition of numpy and tornado to requirements.txt and the update of the token used for code checkout in the GitHub workflow.
## [Updated GitHub Action to Push to HuggingFace Space](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/e95e574c846541fd959bd0d0355178fae542dd8e)
Wed Sep 27 17:05:25 2023 +0000
- This commit modifies the triggering conditions for the GitHub Action workflow that pushes updates to HuggingFace Space. Previously, the workflow was triggered on each push with any tag. Now, it is triggered upon completion of the 'Update AI Changelog on Push to Main' workflow on the 'main' branch.
- Additionally, the 'push-to-huggingface' job has been updated to depend on the completion of the 'update-changelog' job.
## [Updated version number from 0.0.2 to 0.0.5](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/55fa7419137cf54127cbd03114c0c0284397cfd9)
Wed Sep 27 10:56:40 2023 -0400
- The version number in the bumpver configuration file has been updated from 0.0.2 to 0.0.5.
- The image version in the Kubernetes resources file has been updated to match the new version number.
- The __version__ variable in the langchain-streamlit-demo app has been updated to reflect the new version number.
## [Updated page title to include version number](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/783c740fe52c44c3f3d9d5ad78b6c1784fa93e97)
Wed Sep 27 10:46:57 2023 -0400
- The page title of the Streamlit application was previously just the name of the application. The change now includes the version number in the title, which will make it easier to track and verify the version of the application in use.
## [Added 'codellama/CodeLlama-34b-Instruct-hf' to Model Dictionary](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/68f6d34a4cefd91425cbc215f323fbd57dd6e4a7)
Wed Sep 27 10:46:24 2023 -0400
- The commit introduces a new model 'codellama/CodeLlama-34b-Instruct-hf' into the MODEL_DICT dictionary. This update extends the list of models supported by the 'Anyscale Endpoints'.
## [Bumped version from 0.0.1 to 0.0.2](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/9feadf73e8c66425a565c99ce3088249bc4699f1)
Wed Sep 27 00:03:38 2023 -0400
- Updated the version number in bumpver.toml, Kubernetes resources.yaml, and the app.py file of the langchain-streamlit-demo application. The new version is 0.0.2.
## [Updated app version](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/a1065bb282837cf191d30bcb45c638bd15c5b77a)
Wed Sep 27 00:00:28 2023 -0400
- The version number in langchain-streamlit-demo/app.py was updated from 0.0.0 to 0.0.1.
## [Updated image version in Kubernetes resources and bumpver file](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/35cffe74d37db50ad5ae17a6e6af4d2131c1a5c3)
Tue Sep 26 23:59:47 2023 -0400
- In the 'bumpver.toml' file, the image version placeholder in 'kubernetes/resources.yaml' was corrected by removing the unnecessary quotes.
- In the 'kubernetes/resources.yaml' file, the image version for 'langchain-streamlit-demo' was updated from 'latest' to '0.0.1'.
## [Implement versioning and modify GitHub workflows](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/7f34c9b5e16996dcb8eb5cdd3f5cdc86d7bf2b11)
Tue Sep 26 23:58:24 2023 -0400
- Introduced semantic versioning using bumpver. The current version is now tracked in a new file 'bumpver.toml' and also reflected in 'app.py' and the Docker image tag in 'kubernetes/resources.yaml'.
- Modified GitHub workflows 'docker-hub.yml' and 'hf-space.yml' to trigger on new tags instead of pushes to the main branch. The Docker image tag is now the release version instead of the git SHA.
- Removed the step to store the git SHA in 'docker-hub.yml'.
- No functional changes were made to 'langchain-streamlit-demo/app.py' or 'kubernetes/resources.yaml'. The imagePullPolicy remains as 'Always'.
## [Updated requirements.txt for better package management](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/5085ade2d646a2670929e518e78b881ea2ffd0a5)
Tue Sep 26 23:14:05 2023 -0400
- Rolled back langchain package from version 0.0.301 to 0.0.300 to avoid a bug in langchain's chatanthropic.
- Pinned numpy to version 1.22.2 as suggested by Snyk to avoid a vulnerability.
- Reordered the packages for better readability.
## [Added numpy and tornado to requirements.txt to avoid vulnerabilities](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/3f0e220f9f77d561510dd04b09f1c3c509a5b28f)
Tue Sep 26 12:56:59 2023 +0000
- The numpy and tornado packages were added to the requirements.txt file. These packages are not directly required by our application but were added to avoid potential vulnerabilities as suggested by Snyk.
## [Updated token used for code checkout in GitHub workflow](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/b0c4e1ca12f86ea6113ee2c86d38c39d3035f395)
Tue Sep 26 08:56:55 2023 -0400
- In the GitHub Actions workflow file 'ai_changelog.yml', the personal access token used for checking out code has been updated. The token has been changed from 'PAT' to 'WORKFLOW_GIT_ACCESS_TOKEN'.
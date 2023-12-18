# AI CHANGELOG
## [Added PythonCompatibilityInspectionAdvertiser to misc.xml and updated agent_type in python_coder.py](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/04cf693d125a71f61b12ce8f5f8024c79fe9908c)
Mon Dec 18 10:59:56 2023 -0500
- In the misc.xml file, a new component 'PythonCompatibilityInspectionAdvertiser' was added to the project. This component is used for inspecting python compatibility.
- In the python_coder.py file, the default value for the 'agent_type' argument in the 'get_agent' function was changed from 'OPENAI_FUNCTIONS' to 'CHAT_CONVERSATIONAL_REACT_DESCRIPTION'. This change affects the type of agent that is initialized by default when the 'get_agent' function is called.
## [Bumped version from 2.1.0 to 2.1.1](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/5a348f9029a30b49eda60ed7b6d612f9602c8bc8)
Mon Dec 18 10:41:42 2023 -0500
- The current version number in bumpver.toml, the image tag in kubernetes/resources.yaml, and the __version__ variable in langchain-streamlit-demo/app.py have all been updated from 2.1.0 to 2.1.1.
## [Update PyPDF package version](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/fc63706a675b02d7b7db5bb31b81d14da3f17bed)
Mon Dec 18 13:16:53 2023 +0000
- This commit updates the version of the PyPDF package from 3.17.2 to 3.17.3 in the requirements.txt file.
## [Updated langsmith package](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/688f2b15a1d6086d6c81ae06f27495421641ac20)
Mon Dec 18 13:15:37 2023 +0000
- The langsmith package has been updated from version 0.0.69 to 0.0.71 in the requirements.txt file.
## [Updated anthropic package version](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/d0fdfb5eaa95b1628140a0a1650d416220070fb4)
Mon Dec 18 13:15:24 2023 +0000
- The anthropic package in the requirements.txt file has been updated from version 0.7.7 to 0.7.8. No other packages were affected in this commit.
## [Updated OpenAI library version](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/4c03ff5ea6f5c3097a53e0c0c5db36967d5e1e8f)
Mon Dec 18 13:13:17 2023 +0000
- The OpenAI library version in requirements.txt has been updated from 1.3.8 to 1.5.0. This update may include new features, bug fixes, and performance improvements.
## [Updated langchain version](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/00528c803be2d7b84bedf1d5469d269529e8a3db)
Mon Dec 18 12:13:48 2023 +0000
- The langchain package was updated from version 0.0.348 to 0.0.350 in the requirements.txt file. This change was necessary to incorporate the latest features and bug fixes from the langchain package.
## [Updated application version to 2.1.0](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/6a5206daa0170076d2e55f3878204571c03b0dbe)
Wed Dec 13 17:57:20 2023 -0500
- The version of the application has been updated from 2.0.1 to 2.1.0. This change is reflected in the bumpver.toml file, which tracks the current version of the application.
- In addition, the Docker image referenced in the Kubernetes resource configuration file (resources.yaml) has been updated to match the new version.
- Finally, the version number displayed on the application's Streamlit page (app.py) has also been updated to reflect the new version.
## [Added Python Coder Assistant to Application Tools](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/94f9b82dcf0b254853e489743d140c674acb2bb6)
Wed Dec 13 17:54:48 2023 -0500
- In this commit, a Python Coder Assistant was added to the application's tools. This assistant is capable of writing Python code given clear instructions and requirements. It was implemented by importing the 'get_agent' function from the newly created 'python_coder.py' file and adding the resulting 'python_coder_tool' to the 'TOOLS' list.
- The 'python_coder.py' file contains the necessary functions and classes to initialize the Python Coder Assistant, check the code, and submit the code. It also ensures that the code conforms to the black, ruff, and strict mypy standards.
- The 'requirements.txt' file was updated to include the new dependencies required by the Python Coder Assistant, namely 'black', 'mypy', and 'ruff'.
## [Added certifi and requests packages to requirements.txt](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/920ffd4c80beac16450c762c3caab609ede20fd0)
Wed Dec 13 18:16:18 2023 +0000
- The certifi and requests packages were added to the requirements.txt file to avoid potential vulnerabilities. These packages were not directly required, but were pinned by Snyk for security reasons.
## [Enhanced tool descriptions and added 'llm-math' tool](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/13d332463cb60b873e75f45f783ca23cef55de93)
Wed Dec 13 13:09:22 2023 -0500
- The commit enhances the descriptions of the 'web-research-assistant' and 'user-document-chat' tools. It also adds the 'llm-math' tool to the default tools list in the 'app.py' file of the 'langchain-streamlit-demo' project.
- In the 'requirements.txt' file, the 'numexpr' package (version 2.8.8) has been added.
## [Added tool loading functionality and updated assistant description](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/d8714b091e4b40041ac26cd8a2854e5ef34011cb)
Wed Dec 13 10:35:50 2023 -0500
- In this commit, the developer has added a line to load additional tools using the 'load_tools' function from the 'langchain.agents' module. This extends the functionality of the default tools available in the application.
- Additionally, the developer has updated the description of the 'web-research-assistant' tool to provide more context on its usage and cost implications. The updated description advises users to use the assistant sparingly due to its relative expense and suggests using DuckDuckGo for quick facts instead.
## [Bumped version from 2.0.0 to 2.0.1](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/9e698f4a274c4780d013fdfb0110a1f7675b580e)
Wed Dec 13 14:10:39 2023 +0000
- This commit updates the version number across several files. Specifically, it modifies the current version in bumpver.toml, the image version in the Kubernetes resources.yaml, and the __version__ variable in the langchain-streamlit-demo/app.py. All these changes reflect the version bump from 2.0.0 to 2.0.1.
## [Improved chat message display in Streamlit app](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/f15299ef4c3f6d17e1fed55329d9be2683e3e6de)
Wed Dec 13 09:08:41 2023 -0500
- This commit updates the chat history section of the Streamlit app. It adds a check to ensure that a message is only displayed if it has content and is of a recognized type ('ai', 'assistant', 'human', 'user'). This prevents empty or unhandled message types from being displayed, improving the user experience.
## [Update version to 2.0.0](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/870f9c796ca452f131df63efeb5fd22f41b35cb3)
Tue Dec 12 17:23:25 2023 -0500
- The version number in bumpver.toml, kubernetes resources.yaml, and app.py has been updated from 1.1.0 to 2.0.0. This includes updates to the current version in the bumpver configuration, the docker image version in the Kubernetes resources file, and the application version in the app.py file.
## [Added new search tools and updated assistant descriptions](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/1ea3b530f16118973e99729685e5e0be621e8a91)
Tue Dec 12 17:03:20 2023 -0500
- Added DuckDuckGoSearchRun and WikipediaQueryRun to the default tools. Updated the description of 'web-research-assistant' to mention quick facts usage of DuckDuckGo. Also, added these tools to the TOOLS list in the provider's condition.
- Updated the DEFAULT_SYSTEM_PROMPT in defaults.py to emphasize a step-by-step approach.
- Added 'wikipedia==1.4.0' to the requirements.txt file for using the Wikipedia API.
## [Updated pre-commit hooks and refactored Streamlit app](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/5825ff944afc97081a1cc740d0ccf3095a80d697)
Tue Dec 12 16:03:57 2023 -0500
- 1. Updated the pre-commit configuration file to reorder the hooks, replacing the 'mypy' hook with the 'black' hook and vice versa.
- 2. Refactored the Streamlit application 'app.py' by adding a new import statement and restructuring the code for better readability and performance. This includes changes in the way the 'research_assistant_tool' and 'doc_chain_tool' are defined and used, and the addition of the 'get_config' function for creating a configuration dictionary.
- 3. Updated the 'llm_resources.py' file to include 'callbacks' as an argument in the 'get_agent' function, and removed the 'create_retriever_tool' usage from the 'get_runnable' function.
## [Added TODO comments for future development](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/547d578fa19e7542737e6165e21b93c0369f5f4f)
Tue Dec 12 14:50:49 2023 -0500
- This commit includes TODO comments in the app.py file of the langchain-streamlit-demo. These comments outline future development tasks related to the usage of agents in the OpenAI or Azure OpenAI, the usage of runnable, and the addition of these to tools.
## [Added web research assistant and updated dependencies](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/883f3bee29ccd1f670e48245d3ada8d1fd7fd3c9)
Tue Dec 12 14:48:04 2023 -0500
- Added a web research assistant that uses DuckDuckGo's search API to perform web searches and BeautifulSoup to scrape text from the resulting URLs. The assistant then generates a report based on the scraped information.
- Updated the pre-commit configuration to add a dependency on 'types-requests'.
- Refactored the 'get_runnable' function in 'llm_resources.py' to use the new 'get_agent' function, which creates an agent with a set of tools and a chat history.
- Updated 'app.py' to use the new web research assistant, and refactored the code to use the new 'get_agent' function.
- Updated the requirements file to include 'beautifulsoup4' and 'duckduckgo-search'.
## [Enhanced chat functionality in the LLMChain](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/048798b27efb2d8dbe52648fdcf34176a608a296)
Tue Dec 12 14:01:20 2023 -0500
- This commit introduces an enhancement to the chat functionality in the LLMChain. It does so by incorporating the chat history into the get_runnable function. The commit also restructures the import statements in the llm_resources.py file and adds new imports necessary for the enhancement.
- The get_runnable function now takes an additional parameter 'chat_history'. It creates a retriever tool and an OpenAIFunctionsAgent with a prompt that includes system messages and the chat history. An AgentTokenBufferMemory is also initialized with the chat history.
- The agent and the tools are then executed using an AgentExecutor that returns the output of the conversation. This enhancement allows the chatbot to maintain a history of the conversation and use it to provide more context-aware responses.
## [Updated version from 1.0.3 to 1.1.0](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/f9ace4d1dc84d8acfab5d95c489b461362d680d0)
Mon Dec 11 12:36:57 2023 -0500
- The version number in bumpver.toml, kubernetes/resources.yaml, and langchain-streamlit-demo/app.py has been updated from 1.0.3 to 1.1.0.
- In bumpver.toml, the current_version key's value is updated.
- In kubernetes/resources.yaml, the image version of the langchain-streamlit-demo container is updated.
- In langchain-streamlit-demo/app.py, the __version__ variable is updated.
## [Removed BM25Retriever and related dependencies](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/c132355839f407ff11494aeee4ff361a7646e913)
Mon Dec 11 12:31:16 2023 -0500
- In this commit, the use of the BM25Retriever and its related dependencies were removed from the project. This included changes in the 'app.py' and 'llm_resources.py' files where the retriever was being used. The 'get_texts_and_retriever' function was removed from 'llm_resources.py' as it was no longer needed. Additionally, the 'rank_bm25' library was removed from the project's requirements in the 'requirements.txt' file.
## [Updated retriever function and imports in app.py and llm_resources.py](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/e8b1107dfef3f5b1bb104b9e4d1f98095a2228ff)
Mon Dec 11 10:27:19 2023 -0600
- In the app.py file, the import statement was updated to include the 'get_texts_and_multiretriever' function from the 'llm_resources' module. The function 'get_texts_and_retriever_cacheable_wrapper' was also updated to call 'get_texts_and_multiretriever' instead of 'get_texts_and_retriever'.
- In the llm_resources.py file, the function 'get_texts_and_retriever2' was renamed to 'get_texts_and_multiretriever'.
## [Updated OpenAI package version](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/cc740341e378b46896457ff83048b981ff8eadc2)
Mon Dec 11 12:44:43 2023 +0000
- The OpenAI package version in requirements.txt was updated from 1.3.7 to 1.3.8.
## [Updated pypdf version](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/d880411e5d768b13efb25d3d7ac4ead6755a4ff0)
Mon Dec 11 12:44:36 2023 +0000
- The pypdf package version in requirements.txt was updated from 3.17.1 to 3.17.2. This change doesn't affect any other dependencies.
## [Updated langchain version in requirements](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/f23ab029e9e13452f9fe0e41ed48f36f257cdbfb)
Mon Dec 11 12:44:32 2023 +0000
- The version of langchain in the requirements.txt file was updated from 0.0.345 to 0.0.348. No other changes were made.
## [Added new retriever function and updated langchain version](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/09bee796cc0e56bf167cff0d12cbdb233184c376)
Fri Dec 8 15:20:41 2023 -0600
- In the langchain-streamlit-demo/llm_resources.py file, a new function called get_texts_and_retriever2 was added. This function processes uploaded file bytes and returns a list of documents and a BaseRetriever instance. It introduces new retriever classes MultiVectorRetriever and MultiQueryRetriever, and uses InMemoryStore for storage. Also, it generates unique identifiers for each text using the uuid library.
- In the requirements.txt file, the version of the langchain package was updated from 0.0.345 to 0.0.346.
## [Updated Azure endpoint configuration in embeddings_kwargs](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/56dd4e0c90ab9ec09be58c184e6bf100398c9be8)
Thu Dec 7 11:00:31 2023 -0500
- This commit modifies the 'get_texts_and_retriever' function in the 'llm_resources.py' file.
- If 'use_azure' is True and 'azure_kwargs' is provided, the 'azure_endpoint' is now set with the value from 'openai_api_base'.
- This update ensures that the correct Azure endpoint is used when creating AzureOpenAIEmbeddings.
## [Bumped version from 1.0.2 to 1.0.3](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/1c0c6c5c2e58321a2dd5f58c079c070d601e315c)
Thu Dec 7 10:25:07 2023 -0500
- Updated the version number in bumpver.toml, the Docker image version in the Kubernetes resources.yaml, and the application version in the app.py file of the langchain-streamlit-demo.
## [Refactored variable name in AzureChatOpenAI constructor](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/17f45e34541f6182f43665bf6c0fe66b2a725eb8)
Thu Dec 7 10:21:30 2023 -0500
- Changed the variable name 'openai_api_base' to 'azure_endpoint' in the AzureChatOpenAI constructor for clarity and consistency.
## [Update version from 1.0.1 to 1.0.2](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/8fee298d3553974031cad83e42e34b6559df5fe5)
Mon Dec 4 11:27:10 2023 -0500
- The version number has been updated in the following files: `bumpver.toml` (the project's version control file), `kubernetes/resources.yaml` (the Kubernetes resources configuration file), and `langchain-streamlit-demo/app.py` (the application's main Python file).
- In `bumpver.toml`, the `current_version` variable has been updated to `1.0.2`.
- In `kubernetes/resources.yaml`, the Docker image version has been updated to `1.0.2`.
- In `langchain-streamlit-demo/app.py`, the `__version__` variable has been updated to `1.0.2`.
## [Updated package versions in requirements.txt](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/3d7adb3b01d4565d59e4b999c69e2d554fab9f02)
Mon Dec 4 11:11:37 2023 -0500
- This commit updates the versions of several packages in the requirements.txt file. The updated packages include 'langchain', 'langsmith', 'openai', 'streamlit', and 'tiktoken'.
- Such updates are necessary to keep the software up-to-date with the latest improvements, bug fixes, and security patches in the packages that it depends on.
## [Updated version to 1.0.1](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/d15b0d2767d9647dd0b05649e5c1d008fa56920e)
Thu Nov 30 15:19:39 2023 -0500
- The version number in bumpver.toml, the Docker image tag in kubernetes/resources.yaml and the version in langchain-streamlit-demo/app.py have been updated from 1.0.0 to 1.0.1.
## [Refactored error handling and added support for AzureOpenAIEmbeddings](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/ead1471ab8d44f8e1ad885100ba614a8a589de5a)
Thu Nov 30 15:12:53 2023 -0500
- This commit includes two main changes. First, the error handling in 'app.py' was refactored to correct the namespace for 'openai.AuthenticationError'.
- Second, in 'llm_resources.py', the code was updated to include support for 'AzureOpenAIEmbeddings' in addition to the existing 'OpenAIEmbeddings'. This allows the application to use either OpenAI's standard embeddings or Azure's version, depending on the provided configuration.
## [Upgraded project version from 0.3.0 to 1.0.0](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/a338494f3816bbb77360d2f43a515d1cc39cd760)
Wed Nov 29 16:05:50 2023 -0500
- Updated the current version in bumpver.toml from 0.3.0 to 1.0.0.
- Modified the Docker image version in kubernetes/resources.yaml from joshuasundance/langchain-streamlit-demo:0.3.0 to joshuasundance/langchain-streamlit-demo:1.0.0.
- Changed the __version__ variable in langchain-streamlit-demo/app.py from 0.3.0 to 1.0.0.
## [Updated model list, library versions, and code formatting](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/3ca1115e20d1709f4ede77b0ce63fafcf42a362c)
Wed Nov 29 16:01:38 2023 -0500
- 1. In the 'defaults.py' file, the list of models was updated. New models were added and existing model names were updated.
- 2. In the 'llm_resources.py' file, a minor code formatting change was made.
- 3. In the 'requirements.txt' file, the versions of several libraries were updated, including 'anthropic', 'langchain', 'langsmith', and 'openai'.
## [Updated version from 0.2.0 to 0.3.0](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/2d1ba795654b4c65e705f42a92eae7a382cc8e66)
Mon Nov 27 16:46:11 2023 -0500
- The version number has been updated from 0.2.0 to 0.3.0 in multiple files. This includes the bumpver.toml, which controls the project versioning, the Kubernetes resources.yaml, which specifies the Docker image version to use, and the main app.py file, which includes a version number for display in the web app.
## [Updated caching decorator and minor code formatting](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/5cdfa32bdb13c91564a4e175bafe1bc04414d1d8)
Mon Nov 27 14:47:58 2023 -0600
- Replaced the `@st.cache_data` decorator with `@st.cache_resource` in `app.py` for the `get_texts_and_retriever_cacheable_wrapper` function. This change might be due to an update in the library or to utilize a more suitable caching method.
- In `llm_resources.py`, removed an unnecessary line break and added a space for better code readability.
## [Updated OpenAI library version](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/a88ba2b3040ffff0c93d1c6159b6120091f76e37)
Mon Nov 27 12:36:16 2023 +0000
- The OpenAI library version in the project's requirements has been updated from 0.28.1 to 1.3.5. This update may include new features, bug fixes, or performance improvements from the library.
## [Updated langsmith package version](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/b3a6aa254b2acd40593ef0b0167e061cd5beb448)
Mon Nov 27 12:36:12 2023 +0000
- The langsmith package version in requirements.txt was updated from 0.0.63 to 0.0.66.
## [Updated langchain version in requirements.txt](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/d6340145557e4727e4521c530efa8abe16060882)
Mon Nov 27 12:36:07 2023 +0000
- The langchain package version has been updated from 0.0.334 to 0.0.340 in the requirements.txt file. This update may include new features, bug fixes, or performance improvements.
## [Updated anthropic package version](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/264cec5ebc6b618397d3b9449bf5277c3ad53c96)
Mon Nov 27 12:36:01 2023 +0000
- The anthropic package version in requirements.txt was updated from 0.5.0 to 0.7.4. No other dependencies were changed.
## [Updated pypdf version](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/325c8315d4b388c71776a939a5267776940b26ce)
Mon Nov 20 12:35:08 2023 +0000
- The pypdf library was updated from version 3.17.0 to 3.17.1 in the requirements.txt file.
## [Updated project version to 0.2.0](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/97d4687085a8c28a8c0a3a082e9cfa70d2fe853e)
Fri Nov 10 21:30:40 2023 -0500
- The version number in bumpver.toml has been updated from 0.1.2 to 0.2.0.
- In the Kubernetes resources.yaml file, the image version of langchain-streamlit-demo has been updated to reflect the new version.
- The __version__ variable in the app.py file of the langchain-streamlit-demo project has also been updated to 0.2.0.
## [Updated pillow library version](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/f61858c54e1a37f8a7a734ca2c84c66cd62d77e4)
Sat Nov 11 02:07:34 2023 +0000
- The pillow library version was updated from 10.0.0 to 10.0.1 in the requirements.txt file. This change was made to avoid a vulnerability.
## [Updated package versions in requirements.txt](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/d4691b420e22e6b27a3d968f1295d97bb3191376)
Fri Nov 10 21:04:08 2023 -0500
- Updated the versions of the 'langchain', 'langsmith', and 'streamlit' packages in the requirements.txt file.
- Added 'pillow' and 'pyarrow' packages to the requirements.txt file.
- These changes ensure that the project is using the latest and most secure versions of the dependencies.
## [Bumped application version from 0.1.1 to 0.1.2](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/a51a26dd0cf4b33726ac3aa84b41acc103b0c06f)
Wed Nov 1 16:03:52 2023 -0400
- Updated the application version in bumpver.toml, resources.yaml, and app.py. This includes the version used for the Docker image in the Kubernetes deployment configuration.
## [Updated default checkbox value and removed initial chatbot message](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/3d59c85771f67f633f9498ffa3705880576de914)
Wed Nov 1 15:51:00 2023 -0400
- Changed the default value of the 'Document Chat' checkbox to be true if a file is uploaded and false if not.
- Removed the condition that disables the 'Chain Type' dropdown when 'Document Chat' is not selected.
- Eliminated the automatic 'Hello! I'm a helpful AI chatbot. Ask me a question!' message when the chat history is empty.
## [Version Bump to 0.1.1](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/fc0e83182e47a9f41465fa815b286455b10e78f9)
Wed Nov 1 13:58:11 2023 -0400
- This commit represents a version bump from 0.1.0 to 0.1.1. Changes were made in the bumpver.toml file to update the current version. The Docker image reference in the Kubernetes resources.yaml file was also updated to reflect the new version. Lastly, the __version__ variable in the langchain-streamlit-demo/app.py file was updated.
## [Handled additional exception in app.py](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/8a23b378977a263201791101e5a0ebc56e4f5f05)
Wed Nov 1 13:55:35 2023 -0400
- Updated the exception handling in app.py to include LangSmithNotFoundError along with the existing LangSmithError. This change improves the robustness of the error handling mechanism.
## [Updated project version to 0.1.0](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/bbb9f000d8907e12c2aea643fb01e234b8d771bc)
Mon Oct 30 12:03:02 2023 -0400
- The project's version number has been updated from 0.0.16 to 0.1.0 in the bumpver.toml file, kubernetes resource file, and the main application file.
## [Added mistralai/Mistral-7B-Instruct-v0.1 to Anyscale Endpoints](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/d8cef94cffde0307292685d7273a0bf7a0974d02)
Mon Oct 30 11:31:43 2023 -0400
- In the README.md file, a new endpoint mistralai/Mistral-7B-Instruct-v0.1 was added under the section of Anyscale Endpoints.
- In the defaults.py file, the same endpoint was added to the MODEL_DICT dictionary under the key-value pair 'mistralai/Mistral-7B-Instruct-v0.1': 'Anyscale Endpoints'.
- The SUPPORTED_MODELS list was updated accordingly to include this new endpoint.
## [Updated langsmith package version](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/018041a3bdd72aaf3ab62b6eecba51ac18c93bcd)
Mon Oct 30 12:50:15 2023 +0000
- The langsmith package version in requirements.txt has been updated from 0.0.49 to 0.0.53. This update might include bug fixes, new features, or improvements.
## [Updated langchain version in requirements](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/1215664e1bcb9b0a1f7f90a608fa16dc68dbbd0a)
Mon Oct 30 12:49:54 2023 +0000
- The langchain package version in requirements.txt has been updated from 0.0.320 to 0.0.325. This update might include bug fixes, security patches or new features.
## [Bump version from 0.0.15 to 0.0.16](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/04871e0362967e38aceb00aa4fd13818a793ff1a)
Mon Oct 23 12:57:22 2023 -0400
- Updated the current version in bumpver.toml from 0.0.15 to 0.0.16.
- In the Kubernetes resources.yaml, updated the image version for langchain-streamlit-demo from 0.0.15 to 0.0.16.
- In langchain-streamlit-demo/app.py, updated the __version__ variable from 0.0.15 to 0.0.16.
## [Updated package versions in requirements.txt](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/839541a4fc5515d4554a36946001f1cee80f6fdc)
Mon Oct 23 12:49:36 2023 -0400
- Updated the versions of 'anthropic', 'langchain', and 'langsmith' in the requirements file. 'anthropic' is updated from version 0.3.11 to 0.5.0, 'langchain' from 0.0.315 to 0.0.320, and 'langsmith' from 0.0.44 to 0.0.49.
## [Added 'validators' package to requirements](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/a1e0ab15cde332cd8efcba310fb67e25cb990783)
Fri Oct 20 22:54:23 2023 +0000
- The 'validators' package was added to the requirements.txt file. This package is not directly required by the project, but it has been pinned by Snyk to version 0.21.0 or newer to avoid a potential vulnerability.
## [Updated badges in README](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/32f02019c445fb88beb73f00c6ffd0a17ff2a5d3)
Thu Oct 19 15:19:10 2023 -0400
- Replaced the Docker badge with a 'Push to Docker Hub' GitHub Actions workflow badge.
- Added a 'Push to HuggingFace Space' GitHub Actions workflow badge.
- Added an 'Update AI Changelog on Push to Main' GitHub Actions workflow badge.
## [Added Azure OpenAI Service to README](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/3353ff5eaa74c050414bf6b67ac590ac25d19f74)
Thu Oct 19 11:08:36 2023 -0400
- Updated README.md to include Azure OpenAI Service in the list of services and endpoints. A placeholder for configurable endpoints under Azure OpenAI Service has also been added.
## [Added Black component to misc.xml and updated badges in README.md](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/1fb27e8b839a4c3d526da009c05ef3c08a1c2786)
Thu Oct 19 10:49:24 2023 -0400
- The commit introduces two changes:
- 1. A new Black component is added to the .idea/misc.xml file. This suggests that the Black Python code formatter has been configured for the project.
- 2. The README.md file has been updated to include new badges for code maintainability, issues, technical debt, and known vulnerabilities. The order of the existing badges has also been rearranged.
## [Version Bump from 0.0.14 to 0.0.15](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/cc115e36633b7d899076da029c59dda03ca177ec)
Mon Oct 16 14:09:34 2023 -0400
- The version number has been increased from 0.0.14 to 0.0.15. This change has been reflected in the bumpver.toml file, the Kubernetes resources file, and the langchain-streamlit-demo app.py file. The Docker image used in the Kubernetes resources file has also been updated to reflect this new version number.
## [Updated several package versions in requirements.txt](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/cfa1e0b55c4f108b30ff6c7389668f1677f91437)
Mon Oct 16 14:02:49 2023 -0400
- Updated the version of langchain from 0.0.308 to 0.0.315.
- Updated the version of langsmith from 0.0.43 to 0.0.44.
- Updated the version of pypdf from 3.16.2 to 3.16.4.
## [Updated environment variable name in Kubernetes config](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/62281947edc36d93259d723b8b4b63f3b9b646d1)
Fri Oct 6 21:19:03 2023 -0400
- In the Kubernetes configuration file 'resources.yaml', the environment variable name 'SHOW_LANGCHAIN_OPTIONS' was replaced with 'SHOW_LANGSMITH_OPTIONS'. This change reflects an update in the naming convention or the service being used.
## [Bumped application version to 0.0.14](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/eb059075d36e4b09269df5b75dbea1b0e4e22f11)
Fri Oct 6 20:59:11 2023 -0400
- Updated the version of the application in bumpver.toml, kubernetes/resources.yaml, and langchain-streamlit-demo/app.py from 0.0.13 to 0.0.14.
## [Refactored app.py to use Streamlit session state for storing global variables](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/e9f7a777844336b99d3bc8c2270e77e2acb0e7e7)
Fri Oct 6 20:47:25 2023 -0400
- This commit refactors the app.py file of the langchain-streamlit-demo to use Streamlit's session state for storing global variables. This includes API keys, project names, and Azure configurations. A new function 'azure_state_or_default' has been introduced to update the session state for Azure configurations. This change allows for better state management and persistence across multiple sessions.
## [Added input field for Azure OpenAI EMB deployment name](https://github.com/joshuasundance-swca/langchain-streamlit-demo/commit/b44c9a31a33a9b7d3b0e347a0ffe4ea31c068e81)
Fri Oct 6 18:40:55 2023 -0400
- An input field for the Azure OpenAI EMB deployment name has been added to the sidebar of the Streamlit application. This allows users to specify the name of their Azure OpenAI EMB deployment.
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
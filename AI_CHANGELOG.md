# AI CHANGELOG
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
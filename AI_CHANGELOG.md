# AI CHANGELOG
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

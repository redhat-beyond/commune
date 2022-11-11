#Contribution Guide

## Getting Started 

### Prerequisites 
- Install [Vagrant](https://www.vagrantup.com/downloads).
- Install [Virtual Box](https://www.virtualbox.org/wiki/Downloads).
- Install [Python 3.9](https://www.python.org/downloads/).

### Setting up 
1. Fork the repository
2. Clone the repository
3. Create a branch for PR 
4. Push branch and create PR 

### Running Project 
1. `cd <project_directory>` 
1. `vagrant up` 
2. `http://localhost:8000`

## Development process

### Issue

#### Pull Request
1. `git checkout -b <pull_request_name> main 
2. `git add <files>` 
3. `git commit -m <meaningful_commit_message>`
4. Repeat until all features are committed 
5. `git push` 
6. Copy link from Git terminal output to submit PR
7. Link the PR to the relevant issue
8. Assign peers to review 
9. Make sure the PR passes CI checks.

### General Guidelines 
- Create issues and tag others to communicate about development work 
- Use the Slack channel to discuss and seek advice 
- Two completed reviews and approvals from other team members before asking the mentors to review and merge
- Each Pull Request should focus on single responsibility principle.
- **The Pull Request should not break any of the existing functionality**
- The PR description should meaningful 

## Coding guidelines
	Document your code 
	Meaningful commits 
##Getting started
	

### Issue template

• **Title**
Must be clear, concise, and accurately describe what the issue is about.

• **Description**
Must include a clear explanation about the reasons for doing the work. Preferably in the form of a user story
that clearly mentions the stakeholders involved and their wishes.

• **Acceptance criteria**
Must be a list of measurable achievements that indicate the work in the issue is done.

### Reviewing PRs:

1. Always provide constructive feedback
2. Keep your ego out of code reviews
3. Be precise about what needs to be improved
4. Don't just hope for the code to work, Check it yourself!
5. Be strict about temporary code
6. Visualize the bigger picture

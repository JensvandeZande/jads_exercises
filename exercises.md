


# Introduction


# Create github repository
1. Go to github login and create a new repository named: \<name>_mnemonic
2. Set to Private.
3. Add README file.
4. Add python .gitignore
5. Create repo

# Create access token
1. Go to [this](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) website and follow the steps to create personal access token (classic).
2. Set an expiration date pretty far in the future
3. Make sure to mark all fields in the scope section.
4. Generate token and make sure to **SAVE IT SECURELY ON YOUR COMPUTER!!** where you can find it back! 

# Clone repo to local filesystem
1. Open a terminal.
2. Create a directory named projects: `mkdir projects`
3. Navigate to projects directory: `cd projects`
4. Copy the https url of your newly created repo on github. You can get this by clicking on the green code button on your repository page. Next click the copy to clipboard icon.
5. Clone the remote repo to local filesystem: `git clone <your hhtps path>`
6. You will be promted to fill in your github username.
7. When prompted to fill in your password, fill in your newly created access token.
8. Navigate to your new project: `cd <name>_mnemonic`
9. Open visual studio code: `code .`

# Create terminal cheat sheet

1. Create a new branch: `git checkout -b terminal_cheat_sheet`
2. Go to [this](https://terminalcheatsheet.com/) website.
3. Using visual studio code, create a new text named: terminal_cheat_sheet.txt
4. Copy paste the cheat sheet into your newly created file.
5. Add you cheet sheet to the staging area: `git add terminal_cheat_sheet.txt`
6. Commit changes: `git commit -m "add terminal cheat sheet"`
7. Push changes to the remote repo: `git push origin master`
# Exclusion Label Manager for Plex

This script adds or removes Exclusion Labels on your Plex users level.

**Example use case:**</br>
Say you want to create collections you only want visible to specific user(s), you can give the collection a label and then add that label to every other user's "Exclude Labels".
If you have many users, this could be quite the chore. This script does it for you in a jiffy.

Originally made to be used with [Movie Recommendations for Plex](https://github.com/netplexflix/Movie-Recommendations-for-Plex)

![Image](https://github.com/user-attachments/assets/727de427-e19a-4a23-bf57-1d09800a8656)
---

## ✨ Features
- ⚡ **Bulk Operation**: Quickly Add desired exclusion label to all users
- 🗑️ **Quick Removal**: Quickly remove exclusion label from all users
- 🏛️ **Library Selection**: Choose Movies, TV Shows or both
- 🙅🏻 **Exclusion**: Skip specific users
- 🅰️ **Case insensitive**: Case-insensitive username handling

---

## 🛠️ Installation

### 1️⃣ Download the script
Clone the repository:
```sh
git clone https://github.com/netplexflix/Exclusion-Label-Manager-for-Plex.git
cd Exclusion-Label-Manager-for-Plex
```

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) Or simply download by pressing the green 'Code' button above and then 'Download Zip'.

### 2️⃣ Install Dependencies
- Ensure you have [Python](https://www.python.org/downloads/) installed (`>=3.8` recommended)
- Open a Terminal in the script's directory
>[!TIP]
>Windows Users: <br/>
>Go to the script folder (where ELMP.py is).</br>
>Right mouse click on an empty space in the folder and click `Open in Windows Terminal`
- Install the required dependencies:
```sh
pip install -r requirements.txt
```

---

## ⚙️ Configuration
- Open `ELMP.py` in a text editor
- Replace `YOUR_PLEX_TOKEN` with your [Plex Token](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/)
- Save

---

## 🚀 Usage

Run the script with:
```sh
python ELMP.py
```

The script will now ask you
1. If you want to ADD or REMOVE exclusion labels
2. which user(s) to skip. e.g.: `user1, user2, user3`
3. Which section to apply the exclusion to. `1` for Movies, `2` for TV Shows (type `1,2` for both)
   
![Image](https://github.com/user-attachments/assets/6361b894-d0eb-4efa-986e-fdd4bd99bffd)

> [!TIP]
> Windows users can create a batch file for quick launching:
> ```batch
> "C:\Path\To\Python\python.exe" "Path\To\Script\ELMP.py"
> pause
> ```

---

## 🍿 Use Cases
**1:**
- You could use [Movie Recommendations for Plex](https://github.com/netplexflix/Movie-Recommendations-for-Plex) to create a "What Should I Watch?" collection for each of your users, or groups of users, with recommendations tailored to their taste.
- If you want each collection to only be visible to the relevant user(s) you can give the collection itself a label.
- Now you can use this script to exclude every other user from seeing this collection.

**2:**
- [Create a collection with each user's Requests, only visible to them](https://www.reddit.com/r/PleX/comments/12g1aoe/howto_create_a_collection_of_your_users_request)
  
> [!IMPORTANT]
> Make sure you give collections a unique label and NOT the label you use to label the Movies or TV shows themselves!</br>
> Otherwise all Movies and/or TV Shows with that label will be hidden from your users as well. 

> [!IMPORTANT]
> Unfortunately collections pinned to Home are visible to ALL users, regardless of these exclusion labels.
> This has been a bug (or feature..?) in Plex for a long time.
> Until/Unless Plex fixes this, your users will have to go to the collections tab to find their exclusive collection.




---

### ⚠️ Need Help or have Feedback?
- Open an [Issue](https://github.com/netplexflix/Exclusion-Label-Manager-for-Plex/issues) on GitHub
- Join our [Discord](https://discord.gg/VBNUJd7tx3)

---

### ❤️ Support the Project
If you find this project useful, please ⭐ star the repository and share it!

<br/>

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/neekokeen)

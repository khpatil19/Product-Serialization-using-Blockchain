# Product-Serialization-using-Blockchain

## Abstract
In this project, we successfully developed and implemented a blockchain-based solution for product serialization for the pharmaceutical supply chain. Leveraging the decentralized and immutable nature of blockchain technology, we replaced traditional databases with a blockchain network to enhance security and transparency in the supply chain. Our platform allows all stakeholders in the supply chain to verify the authenticity of products and update product details seamlessly, mitigating the risks of counterfeit goods and ensuring product safety.

Through our project, we addressed the limitations of traditional product serialization systems by providing a more secure and transparent approach. Our solution enables users to detect unauthorized tampering and improving supply chain integrity. The use of blockchain technology also enhances data security, as information is encrypted and distributed across the network, reducing the risks of data breaches.

Our completed project has successfully demonstrated the potential of blockchain in improving supply chain management in the pharmaceutical industry. The adoption of our blockchain-based solution has the potential to enhance trust and transparency among stakeholders, ultimately contributing to a safer and more reliable pharmaceutical supply chain ecosystem.

# Setting up the project
Download the project files and keep them stored in a folder on your device. You’ll also need the project files for the android application, which you can download from [this repository](https://github.com/khpatil19/Product-Serialization-App).

In order to run this prototype, you’ll need the following installed on your device:

- [Anaconda Navigator](https://www.anaconda.com/download)
- [Ganache Desktop](https://trufflesuite.com/ganache/)
- [IPFS Desktop](https://docs.ipfs.tech/install/ipfs-desktop/#windows)
- [Android Studio](https://developer.android.com/studio?gclid=Cj0KCQjwmtGjBhDhARIsAEqfDEdCr4YUW5ppilVH1iTiHA75FD4DXdzlg17ZR3APZuLJ_bYoYbSIe28aAhHlEALw_wcB&gclsrc=aw.ds)
- [MetaMask](https://metamask.io/) extension running in your browser

# Running the project

1. Open Anaconda Navigator
    1. From “Applications on” select “project”.
    2. Launch Spyder.
    3. In Spyder, change the running directory next to the Python logo to the location where you’ve stored the project files.
2. Open Ganache.
    1. Select the workspace as *mindspace (ethereum)*.
3. Open IPFS Desktop.
    1. Restart it from the task bar shortcut.
4. Open [Remix Ethereum IDE](https://remix.ethereum.org/) (website)
    1. Paste the solidity code from the project files and save it as *dpharma.sol*
    2. Select the smart contract *dpharma.sol*. Click “Deploy & Run Transactions”
    3. Select the environment as “Dev - Ganache Provider” and tick “Publish to IPFS” below the deploy button.
5. Run *app.py* from Spyder. Copy the IP address (should be something like `192.168.1.8`).
6. Open Android Studio
    1. Import the mobile application (code is in this repository).
    2. Open *URLlinks.java*. Replace the IP with the one generated in the Spyder console. For instance - as per our earlier example, the line should look like `public static String *urlserverpython*="http://192.168.1.7:5000/";`
    3. Ensuring that your mobile device is plugged in via USB cable and on Developer Mode (with USB debugging enabled), run *URLlinks.java*. The app should run on your device.

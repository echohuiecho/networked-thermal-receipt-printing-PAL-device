# Post Anthropocene Learning Device - Networked Thermal Receipt Printing Kiosk
**An interactive art installation with kiosk application and networked thermal printing service**

## :question: About
What if, we pick an alternative narrative to understand plants and nature, such as the perspective of the plant, will it deconstruct our established ideology of nature? And develop a diverse and empathetic way to understand nature and the world?

In this natural history display case like learning device, participants can search for the botanical drawings of 20 kinds of vegetables. Yet it is not going to show the images that you’re familiar with, it will only present the minor and neglected narratives of the plants. Moreover, the participants can print out receipts of their chosen vegetables, with drawings from the learning device, and there is a QR code for them to access online Post Anthropocene Botanical Encyclopedia.

*Post Anthropocene Learning Device* was a collaborated work with Hong Kong artist [Benjamin Hao Lap yan](https://benjaminhao.net/). My role is a creative technologist / new media artist who is responsible to develop the networked receipt printing device with a touch-screen kiosk application and an online Post Anthropocene Botanical Encyclopedia. It was a commissioned project in ARCH “Arts X Tech” Exhibition invited by the [13th Arts Ambassadors-in-School Scheme](https://www.hkadc.org.hk/en/whats-on/past-events/13th-aaiss-youth-arts-week-arts-x-tech-interactive-exhibition) organised by the Hong Kong Arts Development Council (HKADC).
## :hammer: Technologies
- JavaScript
- Vue.js
- Raspberry Pi
- Python
- Flask
- Bootstrap 5
- Sass/SCSS

## :star: Features
### Kiosk Desktop Application
![image](https://uploads-ssl.webflow.com/603fbf7c21375f0867e94c5c/622f04523562b18d711d1b10_MIC02297.jpg)
- The application is developed with Vue.js as frontend and Python Flask Framework as backend
- Users can select the plants on the touch-screen device, a print request will be sent to the thermal printer through the Raspberry Pi

### Networked receipt printing service
![image](https://uploads-ssl.webflow.com/603fbf7c21375f0867e94c5c/622f03d9ec6e56431ad9b4df_MIC02660.jpg)
- A 5V thermal printer is connected to the Raspberry Pi for the printing service
- The print function is developed using CUPS

### Online Post Anthropocene Botanical Encyclopedia
[Live URL](https://pal-device.com/#/)
- A QR code corresponding to each plant is printed on the receipt with the networked thermal printer. Users can access the online Post Anthropocene Botanical Encyclopedia using the QR code or the Desktop application in the exhibition venue
- The desktop application is developed with Electron Framework and Vue.js

#### Image Upload function
The project is planned to expand with a series of workshops for learning the local botanical culture. The Image upload function is developed for future workshop participants.
- The future participants can upload the drawings of their interpretations of local plants.
- The images are uploaded to Cloudinary with [Cloudinary Upload Widget](https://cloudinary.com/documentation/upload_widget)
![image](https://uploads-ssl.webflow.com/603fbf7c21375f0867e94c5c/622f15d75a46634f986ff76e_PAL_device_upload_screen_capture-01.png)
![image](https://uploads-ssl.webflow.com/603fbf7c21375f0867e94c5c/622f163050ce9fe9df8fa266_PAL_device_upload_screen_capture-03.png)

## :thought_balloon: Project Setup
1. Clone this repository to your **Raspberry Pi**
    ```
    git clone https://github.com/echohuiecho/networked-thermal-receipt-printing-PAL-device.git
    ```

### Frontend Setup
1. Go to Frontend directory
   ```
   cd networked-thermal-receipt-printing-PAL-device/frontend
   ```
2. Install the dependencies
    ```
    npm install
    ```
3. Compiles and hot-reloads for development
    ```
    npm run serve
    ```

#### Compiles and minifies for production
```
npm run build
```

### Flask Backend Setup
1. Go to backend directory
    ```
    cd networked-thermal-receipt-printing-PAL-device/backend_flask_RaspberryPi
    ```
2. activate the environment
    ```
    source env/bin/activate
    ```
3. Run the flask application
   ```
   flask run
   ```

## :clap: Acknowledgements
- The networked receipt printing feature is inspired by [this tutorial](https://www.hackster.io/glowascii/using-a-thermal-printer-with-raspberry-pi-d74619) on Hackster.io

## :page_facing_up: License
[CC BY-NC-ND](https://creativecommons.org/licenses/by-nc-nd/4.0/)
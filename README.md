## Warframe Stats for Discord Profile Widgets
### **Experimental Discord Widgets powered by AlecaFrame**

A seamless way to display your Warframe progression and in-game economy directly on your Discord profile using experimental widgets. This guide provides step-by-step instructions on how to leverage the data from AlecaFrame and integrate it into your Discord application.


## Overview

Ever wanted to show off your current wealth, trading stats, or progress in Warframe? 
By leveraging AlecaFrame—the most advanced companion app for Warframe—you can now bridge your in-game data with your Discord presence.

This setup allows you to display live-updating stats like Platinum, Credits, Endo, Aya, Ducats, Account Stats and Trade counts directly on your Discord profile board.

## Prerequisites

Before setting up the data fields, you must ensure your Discord account is prepared for experimental widgets.

Please follow this [Guid](https://chloecinders.com/blog/discord-widgets#setting-up-a-discord-application](https://www.youtube.com/watch?v=gYv7D83u7yQ)](https://www.youtube.com/watch?v=gYv7D83u7yQ) here to properly set up a Discord application and unlock the necessary widget functionalities.


## Configuration Guide

Once your application is set up in the Discord Developer Portal (Games → Widget → your widget).

Widget Layout: Under the widget settings, ensure you select "Widget Bottom" and "Stats Grid" for the layout.

add the following fields. Ensure the Value Type is set to `String` for all entries.

| Data Field name | Type | Explanation |
| :--- | :--- | :--- |
| `Endo` | String 1 | Your current total Endo balance |
| `Platinum` | String 2 | Your available Platinum balance |
| `Credits` | String 3 | Your current credit total |
| `Aya` | String 4 | Your current amount of Aya |
| `Ducats` | String 5 | Your current Ducat balance |
| `Trades` | String 6 | Total number of trades completed |
| `Name` | String 7 | Displays your IGN |
| `MR` | String 8 | Displays your Mastery Rank |

## Setup Instructions
### Follow these steps to link your Warframe data to your Discord profile:

1. **AlecaFrame Setup:**
   Ensure AlecaFrame is installed and running on your PC.
   In AlecaFrame, navigate to the Stats tab.
   
   Click on Create Public Link. Select the following resources: Platinum, Endo, Aya, Trades, Ducats, and Credits. and then Generate Link.
   after that go into the config.json and under `alecaframe_token` paste in the link

2. **Discord Application:**
   
   Follow the [Guid at chloecinders.com](https://chloecinders.com/blog/discord-widgets#setting-up-a-discord-application) to create your Discord application.
   In the Developer Portal, navigate to your application and open the Widget tab under Games.

4. **Connecting Data:**

   Under the Sample Data Fields section of your widget, add the fields listed in the table above.
   Ensure the Value Type is strictly set to `String`. Like This:
   
   <img width="1171" height="322" alt="image" src="https://github.com/user-attachments/assets/6555efa6-89ff-4354-9548-736b18f46ec9" />

   Once you have created the fields, click into each stat to configure the specific appearance.
   Match the settings as shown in this screenshot: ( do this for every string )
   
   <img width="366" height="842" alt="image" src="https://github.com/user-attachments/assets/918ffe7a-d713-4e8e-9864-cb60935c4440" />

   Value: Set Presentation Type to Text, Value Type to User Data, and select the corresponding Data Field `(e.g., Endo)`. Enable the Fallback toggle.
   
   Label: Set Value Type to Custom String and enter your desired label `(e.g., ✨ Endo)`.
   
   Icon: Enable the Icon toggle, set Value Type to Application Asset, and select the appropriate asset key for your icon. ( in this repo are all the icons i used )

5. **Warframe Name and Mastery Rank Display:**
  
   In order to see your Ingame name and Mastery Rank you need to do this:

   **For Ingamename**
   
   first you need to add 2 new `Strings` MR as `String 7` and Name as `String 8`

   Then you go to `Widget Top` and then to `Title`

   Change `Presentation Type` to `Text`

   `Value Type` to `User Data`

   `Data Field` to `Name`

   and enable `Fallback`

   **For Mastery Rank**

   Go to `Widget Top` and then to `Subtitle 1`

   Change `Presentation Type` to `Text`

   `Value Type` to `Custom String`

   `Data Field` to `Mastery Rank`

   Then Go to the `Text` Tab

   Change `Presentation Type` to `Text`

   `Value Type` to `User Data`

   `Data Field` to `MR`

   and activate `Fallback`
   



6. **(Optional) Convert Script to Executable**
   
   Step 1: Ensure you have Python installed on your system.

   Step 2: Install the necessary packaging tool by running pip install pyinstaller in your terminal.

   Step 3: Navigate to your script folder and run the following command:
   pyinstaller --onefile main.py

   Step 5 (Important): Make sure to copy your config.json file into the dist/ folder alongside the newly created .exe. The application requires this file in the same directory to function correctly.


   


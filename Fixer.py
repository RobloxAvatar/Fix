import psutil
from colorama import Fore, Back ,init
from pathlib import Path
import os
from time import sleep

ROBLOX_PATH = Path.home() / "AppData\\Local\\Roblox"
USER_TEMP = Path.home() / "AppData\\Local\\Temp"

init()

print(Fore.RED + "Killing Roblox process")

for proc in psutil.process_iter():
    if proc.name() == "RobloxPlayerBeta":
        proc.kill()

print(Fore.GREEN + "Killed process\n")

print(Fore.WHITE + "--------------------\n")

if Path(ROBLOX_PATH / "GlobalBasicSettings_13.xml").is_file():
	print(Fore.GREEN + "Trying Method #1 - Deleting GlobalBasicSettings_13.xml!")
else:
	print(Fore.GREEN + "Trying Method #1 - Creating GlobalBasicSettings_13.xml!")

if Path(ROBLOX_PATH / "GlobalBasicSettings_13.xml").is_file():
    Path.unlink(ROBLOX_PATH / "GlobalBasicSettings_13.xml")
    print(Fore.GREEN + "File successfully deleted\n")
    sleep(0.25)
    print(Fore.CYAN + "creating GlobalBasicSettings_13.xml file!")
    sleep(1)
    completeName = os.path.join(ROBLOX_PATH, "GlobalBasicSettings_13.xml")
    file1 = open(completeName, "w")
    file1.write('<roblox xmlns:xmime="http://www.w3.org/2005/05/xmlmime" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.roblox.com/roblox.xsd" version="4">' +
	'<External>null</External>' +
	'<External>nil</External>' +
	'<Item class="UserGameSettings" referent="RBX8BD31B0FC07D4AC7A38A941C4FD0439B">'
		'<Properties>' +
			'<bool name="AllTutorialsDisabled">false</bool>' +
			'<BinaryString name="AttributesSerialize"></BinaryString>' +
			'<token name="CameraMode">0</token>' +
			'<bool name="CameraYInverted">false</bool>' +
			'<bool name="ChatVisible">true</bool>' +
			'<string name="CompletedTutorials"></string>' +
			'<bool name="ComputerCameraMovementChanged">false</bool>' +
			'<token name="ComputerCameraMovementMode">0</token>' +
			'<bool name="ComputerMovementChanged">false</bool>' +
			'<token name="ComputerMovementMode">0</token>' +
			'<token name="ControlMode">1</token>' +
			'<bool name="Fullscreen">false</bool>' +
			'<float name="GamepadCameraSensitivity">1</float>' +
			'<int name="GraphicsQualityLevel">3</int>' +
			'<bool name="HasEverUsedVR">false</bool>' +
			'<float name="MasterVolume">1</float>' +
			'<bool name="MicroProfilerWebServerEnabled">false</bool>' +
			'<float name="MouseSensitivity">0.400000006</float>' +
			'<Vector2 name="MouseSensitivityFirstPerson">' +
				'<X>0.400000006</X>' +
				'<Y>0.400000006</Y>' +
			'</Vector2>' +
			'<Vector2 name="MouseSensitivityThirdPerson">' +
				'<X>0.400000006</X>' +
				'<Y>0.400000006</Y>' +
			'</Vector2>' +
			'<string name="Name">GameSettings</string>' +
			'<bool name="OnScreenProfilerEnabled">false</bool>' +
			'<bool name="PerformanceStatsVisible">false</bool>' +
			'<int name="RCCProfilerRecordFrameRate">0</int>' +
			'<int name="RCCProfilerRecordTimeFrame">0</int>' +
			'<token name="SavedQualityLevel">1</token>' +
			'<int64 name="SourceAssetId">-1</int64>' +
			'<bool name="StartMaximized">true</bool>' +
			'<Vector2 name="StartScreenPosition">' +
				'<X>-8</X>' +
				'<Y>-8</Y>' +
			'</Vector2>' +
			'<Vector2 name="StartScreenSize">' +
				'<X>1552</X>' +
				'<Y>840</Y>' +
			'</Vector2>' +
			'<BinaryString name="Tags"></BinaryString>' +
			'<bool name="TouchCameraMovementChanged">false</bool>' +
			'<token name="TouchCameraMovementMode">0</token>' +
			'<bool name="TouchMovementChanged">false</bool>' +
			'<token name="TouchMovementMode">0</token>' +
			'<bool name="UsedCoreGuiIsVisibleToggle">false</bool>' +
			'<bool name="UsedCustomGuiIsVisibleToggle">false</bool>' +
			'<bool name="UsedHideHudShortcut">false</bool>' +
			'<bool name="VREnabled">true</bool>' +
			'<int name="VRRotationIntensity">1</int>' +
			'<string name="gaID"></string>' +
		'</Properties>' +
	'</Item>' +
'</roblox>')
else:
    completeName = os.path.join(ROBLOX_PATH, "GlobalBasicSettings_13.xml")
    file1 = open(completeName, "w")
    file1.write('<roblox xmlns:xmime="http://www.w3.org/2005/05/xmlmime" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.roblox.com/roblox.xsd" version="4">' +
	'<External>null</External>' +
	'<External>nil</External>' +
	'<Item class="UserGameSettings" referent="RBX8BD31B0FC07D4AC7A38A941C4FD0439B">'
		'<Properties>' +
			'<bool name="AllTutorialsDisabled">false</bool>' +
			'<BinaryString name="AttributesSerialize"></BinaryString>' +
			'<token name="CameraMode">0</token>' +
			'<bool name="CameraYInverted">false</bool>' +
			'<bool name="ChatVisible">true</bool>' +
			'<string name="CompletedTutorials"></string>' +
			'<bool name="ComputerCameraMovementChanged">false</bool>' +
			'<token name="ComputerCameraMovementMode">0</token>' +
			'<bool name="ComputerMovementChanged">false</bool>' +
			'<token name="ComputerMovementMode">0</token>' +
			'<token name="ControlMode">1</token>' +
			'<bool name="Fullscreen">false</bool>' +
			'<float name="GamepadCameraSensitivity">1</float>' +
			'<int name="GraphicsQualityLevel">3</int>' +
			'<bool name="HasEverUsedVR">false</bool>' +
			'<float name="MasterVolume">1</float>' +
			'<bool name="MicroProfilerWebServerEnabled">false</bool>' +
			'<float name="MouseSensitivity">0.400000006</float>' +
			'<Vector2 name="MouseSensitivityFirstPerson">' +
				'<X>0.400000006</X>' +
				'<Y>0.400000006</Y>' +
			'</Vector2>' +
			'<Vector2 name="MouseSensitivityThirdPerson">' +
				'<X>0.400000006</X>' +
				'<Y>0.400000006</Y>' +
			'</Vector2>' +
			'<string name="Name">GameSettings</string>' +
			'<bool name="OnScreenProfilerEnabled">false</bool>' +
			'<bool name="PerformanceStatsVisible">false</bool>' +
			'<int name="RCCProfilerRecordFrameRate">0</int>' +
			'<int name="RCCProfilerRecordTimeFrame">0</int>' +
			'<token name="SavedQualityLevel">1</token>' +
			'<int64 name="SourceAssetId">-1</int64>' +
			'<bool name="StartMaximized">true</bool>' +
			'<Vector2 name="StartScreenPosition">' +
				'<X>-8</X>' +
				'<Y>-8</Y>' +
			'</Vector2>' +
			'<Vector2 name="StartScreenSize">' +
				'<X>1552</X>' +
				'<Y>840</Y>' +
			'</Vector2>' +
			'<BinaryString name="Tags"></BinaryString>' +
			'<bool name="TouchCameraMovementChanged">false</bool>' +
			'<token name="TouchCameraMovementMode">0</token>' +
			'<bool name="TouchMovementChanged">false</bool>' +
			'<token name="TouchMovementMode">0</token>' +
			'<bool name="UsedCoreGuiIsVisibleToggle">false</bool>' +
			'<bool name="UsedCustomGuiIsVisibleToggle">false</bool>' +
			'<bool name="UsedHideHudShortcut">false</bool>' +
			'<bool name="VREnabled">true</bool>' +
			'<int name="VRRotationIntensity">1</int>' +
			'<string name="gaID"></string>' +
		'</Properties>' +
	'</Item>' +
'</roblox>')
print(Fore.GREEN + "Successfully created the file!\n")

print(Fore.WHITE + "--------------------\n")

print(Fore.RED + "If doesn't work remove your Roblox client" + Fore.RESET)
input("Press any key for exit")

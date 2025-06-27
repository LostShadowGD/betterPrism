import pygame
from pygame.locals import *
import time
import subprocess
from subprocess import Popen
import os
import sys
import threading
import platform
import webbrowser

version = "v1.0"

global loading
loading = False
macFontError = False
global settingsOpen
settingsOpen = False

with open("config/instance.txt", "r") as file:
    instance = file.read().strip()

with open("config/titleType.txt", "r") as file:
    titleType = file.read().strip()

if titleType == "advanced":
    windowTitle = "betterPrism " + version + ", running instance " + instance + ", with pygame " + pygame.version.ver + " (" + titleType +" title type)"
else:
    windowTitle = "betterPrism " + version

def run_in_new_console(command):
    if platform.system() == "Windows":
        Popen(command, creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif platform.system() == "Darwin":
        # macOS: open a new Terminal window and run the command
        script = f'''osascript -e 'tell application "Terminal" to do script "{command}"' '''
        Popen(["/bin/bash", "-c", script])
    else:
        # Linux: open a new terminal window (example with gnome-terminal)
        Popen(["gnome-terminal", "--", "bash", "-c", command])

def launchInstance():
    if platform.system() == "Windows":
        prismDir = os.path.join(os.environ["LOCALAPPDATA"], "Programs", "PrismLauncher")
        print(prismDir)
        launchCommand = prismDir + "\prismlauncher.exe --launch " + instance
    elif platform.system() == "Darwin":
        prismDir = "/Applications/PrismLauncher.app/Contents/MacOS/PrismLauncher"
        print(prismDir)
        launchCommand = prismDir + " --launch " + instance

    print(launchCommand)
    Popen(launchCommand, creationflags=subprocess.CREATE_NEW_CONSOLE)

def instanceSelectStart():
    global loading
    loading = True

def instanceSelect():
    global loading
    instanceSelectCommand = """py libchoice.py -q "Instance" --file config/instance.txt -ot s"""
    p = Popen(instanceSelectCommand, creationflags=subprocess.CREATE_NEW_CONSOLE)
    
    p.wait()

    loading = False
    Popen("betterPrism.exe")
    sys.exit()

def titleTypeChoiceStart():
    global loading
    loading = True

def titleTypeChoice():
    global loading
    titleTypeChoiceCommand = """py libchoice.py -q "Title Type" --file config/titleType.txt -ot m -o basic,advanced"""
    p = Popen(titleTypeChoiceCommand, creationflags=subprocess.CREATE_NEW_CONSOLE)
    
    p.wait()

    loading = False
    Popen("betterPrism.exe")
    sys.exit()

def modManager():
    run_in_new_console('py MCModManager.py')

def resManager():
    run_in_new_console('py MCResManager.py')

def showInstance():
    if platform.system() == "Windows":
        prismDir = os.path.join(os.environ["LOCALAPPDATA"], "Programs", "PrismLauncher")
        print(prismDir)
        showCommand = prismDir + "\prismlauncher.exe --show " + instance
    elif platform.system() == "Darwin":
        prismDir = "/Applications/PrismLauncher.app/Contents/MacOS/PrismLauncher"
        print(prismDir)
        showCommand = prismDir + " --show " + instance
    print(showCommand)
    Popen(showCommand, creationflags=subprocess.CREATE_NEW_CONSOLE)

def resolveFontError():
    webbrowser.open("https://developer.apple.com/download/files/SF-Pro.dmg")

def settingsPage():
    global settingsOpen
    settingsOpen = True


bgColour = (40,40,40)
icon = pygame.image.load("assets/logo.png")
w = 800
h = 450

launchBtn = pygame.image.load("assets/launchBtn.png")
launchRect = launchBtn.get_rect()
launchRect.center = w//2 + 120, h//2 + 120

instanceBG = pygame.image.load("assets/instanceBG.png")
instanceBGRect = instanceBG.get_rect()
instanceBGRect.center = 520, 423

instanceBtn = pygame.image.load("assets/instanceBtn.png")
instanceRect = instanceBtn.get_rect()
instanceRect.center = w//2 + 210, 423

settingBtn = pygame.image.load("assets/aboutBtn.png")
settingRect = settingBtn.get_rect()
settingRect.center = w//2 + 394, 435

bgImg = pygame.image.load("assets/mcBGimage.png")
bgImgRect = bgImg.get_rect()
bgImgRect.center = w//2, h//2

modMgrBtn = pygame.image.load("assets/modMgrBtn.png")
modMgrBtnRect = modMgrBtn.get_rect()
modMgrBtnRect.center = w//2 - 272, h//2 - 125

logoText = pygame.image.load("assets/logoText.png")
logoTextRect = logoText.get_rect()
logoTextRect.center = w//2 + 120, h//2 - 180

resMgrBtn = pygame.image.load("assets/resMgrBtn.png")
resMgrBtnRect = resMgrBtn.get_rect()
resMgrBtnRect.center = w//2 - 272, h//2 - 40

showInstanceBtn = pygame.image.load("assets/showInstanceBtn.png")
showInstanceBtnRect = showInstanceBtn.get_rect()
showInstanceBtnRect.center = 520 - 172 - 24, 423

fontError = pygame.image.load("assets/fontError.png")
fontErrorRect = fontError.get_rect()
fontErrorRect.center = w//2, h//2

loadOverlay = pygame.image.load("assets/loadOverlay.png")
loadOverlayRect = fontError.get_rect()
loadOverlayRect.center = w//2, h//2

homeBtn = pygame.image.load("assets/homeBtn.png")
homeBtnRect = homeBtn.get_rect()
homeBtnRect.center = w//2 + 374, 435

aboutLogo = pygame.image.load("assets/aboutLogo.png")
aboutLogoRect = aboutLogo.get_rect()
aboutLogoRect.center = w//2 - 200, 20 + 40

prismLauncher = pygame.image.load("assets/prismLauncher.png")
prismLauncherRect = prismLauncher.get_rect()
prismLauncherRect.center = w//2 - 150, h // 2

minecraft = pygame.image.load("assets/minecraft.png")
minecraftRect = minecraft.get_rect()
minecraftRect.center = w//2 + 150, h // 2

titleTypeBtn = pygame.image.load("assets/titleTypeBtn.png")
titleTypeBtnRect = titleTypeBtn.get_rect()
titleTypeBtnRect.center = w//2 + 374, 405

pygame.init()
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption(windowTitle)

if platform.system() == "Windows":
    bodyFont = pygame.font.SysFont("Segoe UI", 18)
    headingFont = pygame.font.SysFont("Segoe UI Semibold", 32)
    titleFont = pygame.font.SysFont("Segoe UI Semibold", 52)
elif platform.system() == "Darwin":
    def is_font_available(name: str) -> bool:
        name = name.replace(" ", "").lower()
        return name in pygame.font.get_fonts()

    sf1 = "SF Pro Display"
    sf2 = "SF Pro Display"

    fonts_available = all(is_font_available(f) for f in [sf1, sf2])

    if fonts_available:
        bodyFont = pygame.font.SysFont("SF Pro Display Regular", 18)
        headingFont = pygame.font.SysFont("SF Pro Display Heavy", 32)
        titleFont = pygame.font.SysFont("SF Pro Display Heavy", 52)
        macFontError = False
    else:
        macFontError = True
        bodyFont = pygame.font.SysFont("Arial", 18)
        headingFont = pygame.font.SysFont("Arial", 32)
        titleFont = pygame.font.SysFont("Arial", 52)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if macFontError:
                if fontErrorRect.collidepoint(mouse_pos):
                    resolveFontError()
            else:
                if launchRect.collidepoint(mouse_pos):
                    launchInstance()
                if instanceRect.collidepoint(mouse_pos):
                    selectType = "instance"
                    loading = True
                    instanceSelectStart()
                if modMgrBtnRect.collidepoint(mouse_pos):
                    modManager()
                if resMgrBtnRect.collidepoint(mouse_pos):
                    resManager()
                if showInstanceBtnRect.collidepoint(mouse_pos):
                    showInstance()
                if settingRect.collidepoint(mouse_pos):
                    if settingsOpen:
                        settingsOpen = False
                    else:
                        settingsPage()
                if titleTypeBtnRect.collidepoint(mouse_pos):
                    selectType = "titleType"
                    loading = True
                    titleTypeChoiceStart()
            
    screen.fill(bgColour)

    settingBtn.convert()
    screen.blit(settingBtn, settingRect)

    if settingsOpen == False:
        bgImg.convert()
        screen.blit(bgImg, bgImgRect)

        launchBtn.convert()
        screen.blit(launchBtn, launchRect)

        instanceBG.convert()
        screen.blit(instanceBG, instanceBGRect)

        instanceBtn.convert()
        screen.blit(instanceBtn, instanceRect)

        modMgrBtn.convert()
        screen.blit(modMgrBtn, modMgrBtnRect)

        logoText.convert()
        screen.blit(logoText, logoTextRect)

        resMgrBtn.convert()
        screen.blit(resMgrBtn, resMgrBtnRect)

        showInstanceBtn.convert()
        screen.blit(showInstanceBtn, showInstanceBtnRect)

        instanceText = bodyFont.render(instance, True, (255, 255, 255))
        screen.blit(instanceText, (380, 410))

        if platform.system() == "Windows":
            modText = headingFont.render("Options", True, (255, 255, 255))
            screen.blit(modText, (70, 10))
        elif platform.system() == "Darwin":
            modText = headingFont.render("Options", True, (255, 255, 255))
            screen.blit(modText, (65, 15))

        if macFontError:
            fontError.convert()
            screen.blit(fontError, fontErrorRect)

        if loading:
            loadOverlay.convert()
            screen.blit(loadOverlay, loadOverlayRect)

    if settingsOpen:
        if platform.system() == "Windows":
            modText = titleFont.render("betterPrism", True, (255, 255, 255))
            screen.blit(modText, ((w // 2) - 143, 20))
        elif platform.system() == "Darwin":
            modText = titleFont.render("betterPrism", True, (255, 255, 255))
            screen.blit(modText, ((w // 2) - 143, 25))
        
        homeBtn.convert()
        screen.blit(homeBtn, homeBtnRect)

        if platform.system() == "Windows":
            modText = bodyFont.render("by LostShadowGD", True, (255, 255, 255))
            screen.blit(modText, (((w // 2) - 143) + 200, 20 + 70))
        elif platform.system() == "Darwin":
            modText = bodyFont.render("by LostShadowGD", True, (255, 255, 255))
            screen.blit(modText, (((w // 2) - 143) + 200, 25 + 75))

        if platform.system() == "Windows":
            modText = bodyFont.render("betterPrism " + version + ", running instance " + instance + ", with pygame " + pygame.version.ver + " (" + titleType +" title type)", True, (255, 255, 255))
            screen.blit(modText, (10, 450 - 30))
        elif platform.system() == "Darwin":
            modText = bodyFont.render("betterPrism " + version + ", running instance " + instance + ", with pygame " + pygame.version.ver + " (" + titleType +" title type)", True, (255, 255, 255))
            screen.blit(modText, (10, 450 - 35))

        aboutLogo.convert()
        screen.blit(aboutLogo, aboutLogoRect)

        prismLauncher.convert()
        screen.blit(prismLauncher, prismLauncherRect)

        minecraft.convert()
        screen.blit(minecraft, minecraftRect)

        titleTypeBtn.convert()
        screen.blit(titleTypeBtn, titleTypeBtnRect)

    pygame.display.update()

    if loading:
        if selectType == "instance":
            instanceSelect()
        if selectType == "titleType":
            titleTypeChoice()

pygame.quit()
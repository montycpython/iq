__doc__ = "Howard Gardner's Theory of Multiple Intelligences"
from androidhelper import Android as beth
bod = beth()

info = """
Algorithms: Machine learning, neural networks, decision trees, clustering, etc.
Data structures: Arrays, linked lists, trees, graphs, etc. for storing and processing data
Object-oriented programming: Classes, objects, inheritance, polymorphism for organizing code
Functional programming: Pure functions, immutability, recursion for composing functions
Dynamic programming: Memoization, tabulation for optimizing computations
Linear algebra: Matrix operations, vector spaces for machine learning and computer vision
Probability and statistics: Random processes, hypothesis testing, regression for modeling uncertainty
"""

intels = {
	'Linguistic Intelligence': 
"""ability to understand and use language \
effectively""",
	'Logical-Mathematical Intelligence': 
"""ability to reason abstractly and think \
logically""",
	'Spatial Intelligence': 
"""ability to think in terms of space and visual \
imagery""",
    'Bodily-Kinesthetic Intelligence': 
"""ability to control body movements and \
manipulate objects""", 
    'Musical Intelligence': 
"""ability to perceive, create, and appreciate \
music""",
    'Interpersonal Intelligence': 
"""ability to understand and interact with \
others""",
    'Intrapersonal Intelligence': 
"""ability to understand oneself and one's \
thoughts and feelings""",
    'Naturalistic Intelligence': 
"""ability to understand and appreciate the \
natural world""",
    'Existential Intelligence': 
"""ability to understand and contemplate \
abstract ideas and concepts""",
    'Moral Intelligence': 
"""ability to understand and apply moral \
principles and values""",
    'Creative Intelligence': 
"""ability to generate new and original \
ideas""",
    'Emotional Intelligence': 
"""ability to recognize and understand emotions \
in oneself and others"""
}

options = ['addContextMenuItem', 
'addOptionsMenuItem', 'batteryGetHealth', 
'batteryGetLevel', 'batteryGetStatus', 
'batteryGetTemperature', 'batteryGetVoltage', 
'cameraInteractiveCapturePicture', 
'cameraStartPreview', 'cameraStopPreview', 
'clearContextMenu', 'clearOptionsMenu', 
'dialogCreateAlert', 'dialogCreateDatePicker', 
'dialogCreateHorizontalProgress', 
'dialogCreateInput', 'dialogCreatePassword', 
'dialogCreateSeekBar', 
'dialogCreateSpinnerProgress', 
'dialogCreateTimePicker', 'dialogDismiss', 
'dialogGetInput', 'dialogGetPassword', 
'dialogGetResponse', 'dialogGetSelectedItems', 
'dialogSetCurrentProgress', 'dialogSetItems', 
'dialogSetMaxProgress', 
'dialogSetMultiChoiceItems', 
'dialogSetNegativeButtonText', 
'dialogSetNeutralButtonText', 
'dialogSetPositiveButtonText', 
'dialogSetSingleChoiceItems', 'dialogShow', 
'fullDismiss', 'fullQuery', 'fullQueryDetail', 
'fullSetList', 'fullSetProperty', 'fullShow', 
'geocode', 'getCellLocation', 'getClipboard', 
'getInput', 'getLastKnownLocation', 
'getLaunchableApplications', 'getPassword', 
'launch', 'log', 'makeToast', 'mediaIsPlaying', 
'mediaPlay', 'mediaPlayClose', 'mediaPlayList', 
'mediaPlayPause', 'mediaPlaySeek', 
'mediaPlaySetLooping', 'mediaPlayStart', 
'notify', 'phoneCall', 'phoneCallNumber', 
'phoneDial', 'phoneDialNumber', 'readLocation', 
'readPhoneState', 'readSensors', 
'recognizeSpeech', 'recorderCaptureVideo', 
'recorderStartMicrophone', 'recorderStartVideo', 
'recorderStop', 'scanBarcode', 'search', 
'sendEmail', 'sensorsGetLight', 
'sensorsReadAccelerometer', 
'sensorsReadMagnetometer', 
'sensorsReadOrientation', 'setClipboard', 
'smsGetMessages', 'smsMarkMessageRead', 
'smsSend', 'startInteractiveVideoRecording', 
'startLocating', 'startSensing', 'startSensingTimed', 
'stopLocating', 'stopSensing', 'ttsIsSpeaking', 
'ttsSpeak', 'viewHtml', 'webViewShow', 
'webcamAdjustQuality', 'webcamStart', 
'webcamStop']

def main():
    print(intels)
    
def dictChef():
    #requires global info
    iqs = {}
    for data in info:
        x = data.split(": ")
        iqs.update({x[0]:x[1].rstrip()})
    grab(iqs)
    
def grab(item):
    print(item)
    bod.setClipboard(str(item))
    bod.makeToast("It's in the 🛍️.")
    return item

def sift(thing):
    __doc__ = "sift thru an object's methods"
    bag = []
    for i in dir(thing):
        x = input(f"Keep - {i}??")
        if bool(x):
            bag.append(i)
    grab(bag)

if __name__ == "__main__":
    main()
 __doc__ = "Howard Gardner's Theory of Multiple Intelligences"
from androidhelper import Android as beth
bod = beth()

info = """
Algorithms: Machine learning, neural networks, decision trees, clustering, etc.
Data structures: Arrays, linked lists, trees, graphs, etc. for storing and processing data
Object-oriented programming: Classes, objects, inheritance, polymorphism for organizing code
Functional programming: Pure functions, immutability, recursion for composing functions
Dynamic programming: Memoization, tabulation for optimizing computations
Linear algebra: Matrix operations, vector spaces for machine learning and computer vision
Probability and statistics: Random processes, hypothesis testing, regression for modeling uncertainty
"""

intels = {
	'Linguistic Intelligence': 
"""ability to understand and use language \
effectively""",
	'Logical-Mathematical Intelligence': 
"""ability to reason abstractly and think \
logically""",
	'Spatial Intelligence': 
"""ability to think in terms of space and visual \
imagery""",
    'Bodily-Kinesthetic Intelligence': 
"""ability to control body movements and \
manipulate objects""", 
    'Musical Intelligence': 
"""ability to perceive, create, and appreciate \
music""",
    'Interpersonal Intelligence': 
"""ability to understand and interact with \
others""",
    'Intrapersonal Intelligence': 
"""ability to understand oneself and one's \
thoughts and feelings""",
    'Naturalistic Intelligence': 
"""ability to understand and appreciate the \
natural world""",
    'Existential Intelligence': 
"""ability to understand and contemplate \
abstract ideas and concepts""",
    'Moral Intelligence': 
"""ability to understand and apply moral \
principles and values""",
    'Creative Intelligence': 
"""ability to generate new and original \
ideas""",
    'Emotional Intelligence': 
"""ability to recognize and understand emotions \
in oneself and others"""
}

options = ['addContextMenuItem', 
'addOptionsMenuItem', 'batteryGetHealth', 
'batteryGetLevel', 'batteryGetStatus', 
'batteryGetTemperature', 'batteryGetVoltage', 
'cameraInteractiveCapturePicture', 
'cameraStartPreview', 'cameraStopPreview', 
'clearContextMenu', 'clearOptionsMenu', 
'dialogCreateAlert', 'dialogCreateDatePicker', 
'dialogCreateHorizontalProgress', 
'dialogCreateInput', 'dialogCreatePassword', 
'dialogCreateSeekBar', 
'dialogCreateSpinnerProgress', 
'dialogCreateTimePicker', 'dialogDismiss', 
'dialogGetInput', 'dialogGetPassword', 
'dialogGetResponse', 'dialogGetSelectedItems', 
'dialogSetCurrentProgress', 'dialogSetItems', 
'dialogSetMaxProgress', 
'dialogSetMultiChoiceItems', 
'dialogSetNegativeButtonText', 
'dialogSetNeutralButtonText', 
'dialogSetPositiveButtonText', 
'dialogSetSingleChoiceItems', 'dialogShow', 
'fullDismiss', 'fullQuery', 'fullQueryDetail', 
'fullSetList', 'fullSetProperty', 'fullShow', 
'geocode', 'getCellLocation', 'getClipboard', 
'getInput', 'getLastKnownLocation', 
'getLaunchableApplications', 'getPassword', 
'launch', 'log', 'makeToast', 'mediaIsPlaying', 
'mediaPlay', 'mediaPlayClose', 'mediaPlayList', 
'mediaPlayPause', 'mediaPlaySeek', 
'mediaPlaySetLooping', 'mediaPlayStart', 
'notify', 'phoneCall', 'phoneCallNumber', 
'phoneDial', 'phoneDialNumber', 'readLocation', 
'readPhoneState', 'readSensors', 
'recognizeSpeech', 'recorderCaptureVideo', 
'recorderStartMicrophone', 'recorderStartVideo', 
'recorderStop', 'scanBarcode', 'search', 
'sendEmail', 'sensorsGetLight', 
'sensorsReadAccelerometer', 
'sensorsReadMagnetometer', 
'sensorsReadOrientation', 'setClipboard', 
'smsGetMessages', 'smsMarkMessageRead', 
'smsSend', 'startInteractiveVideoRecording', 
'startLocating', 'startSensing', 'startSensingTimed', 
'stopLocating', 'stopSensing', 'ttsIsSpeaking', 
'ttsSpeak', 'viewHtml', 'webViewShow', 
'webcamAdjustQuality', 'webcamStart', 
'webcamStop']

def main():
    print(intels)
    
def dictChef():
    #requires global info
    iqs = {}
    for data in info:
        x = data.split(": ")
        iqs.update({x[0]:x[1].rstrip()})
    grab(iqs)
    
def grab(item):
    print(item)
    bod.setClipboard(str(item))
    bod.makeToast("It's in the 🛍️.")
    return item

def sift(thing):
    __doc__ = "sift thru an object's methods"
    bag = []
    for i in dir(thing):
        x = input(f"Keep - {i}??")
        if bool(x):
            bag.append(i)
    grab(bag)

if __name__ == "__main__":
    main()
 

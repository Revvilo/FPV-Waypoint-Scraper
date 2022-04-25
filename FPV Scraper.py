from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URLs = """https://minecraftfpv.com/track/1EB686D9178F68009452FD475F215E45
https://minecraftfpv.com/track/1EC6E1E1AF1A6142894CD75ED261F65F
https://minecraftfpv.com/track/1EC6BF238F716FB98120AFEE8850845E
https://minecraftfpv.com/track/1EB2C39E1FEC6453926F3DBB8C6C0196
https://minecraftfpv.com/track/1EC73E084C2F63F49588D17AD27E4347
https://minecraftfpv.com/track/1EC6E3C3570564D3894CD75ED261F65F
https://minecraftfpv.com/track/1EC8C5942D076B9E9F2BD5A296FA7C2F
https://minecraftfpv.com/track/1EB9099ABBF96F57B66B7DA8C396EFA0
https://minecraftfpv.com/track/1EC78690853C66D4B131C92F1C5DCDCD
https://minecraftfpv.com/track/1EC77B7D356964F4B131C92F1C5DCDCD
https://minecraftfpv.com/track/1EC7496AA1406DD492DE8F43CBD6AD2C
https://minecraftfpv.com/track/1EB4262B44346E858705F135F65B5917
https://minecraftfpv.com/track/1EC6DD6997DC6C72894CD75ED261F65F
https://minecraftfpv.com/track/1EB909981E116607B66B7DA8C396EFA0
https://minecraftfpv.com/track/1EC6C797885A65F69C8107883A430151
https://minecraftfpv.com/track/1EC75305B956651A92DE8F43CBD6AD2C
https://minecraftfpv.com/track/1EC6DA60537E62A9894CD75ED261F65F
https://minecraftfpv.com/track/1EC6A65D370D6170988BC704B21426E3
https://minecraftfpv.com/track/1EB231DA0DC066BDA86B19FF60E0444E
https://minecraftfpv.com/track/1EC6FE0AFAF260F59F5D8D80F36BBAC4
https://minecraftfpv.com/track/1EC763A0FC8064818CC521BB3C70704C
https://minecraftfpv.com/track/1EC72520B02068BAABC7FFF541AEEDA1
https://minecraftfpv.com/track/1EB239E48EA16FEE9900D32A287E63A8
https://minecraftfpv.com/track/1EB42625D1EC6DF58705F135F65B5917
https://minecraftfpv.com/track/1EC8F1E8113766F4902365312A4A818B
https://minecraftfpv.com/track/1EB9221CAAB963778509ED68055741F2
https://minecraftfpv.com/track/1EC72FA713716B02BE661D29F3C9BA71
https://minecraftfpv.com/track/1EC8C2BCF8AD6FEE9F2BD5A296FA7C2F
https://minecraftfpv.com/track/1EB923A5E7026C06B905BB7F911845B1
https://minecraftfpv.com/track/1EB27E3D92196CA795C32B6F2FB63C75
https://minecraftfpv.com/track/1EB43DE591196FC5B5D5857D258318A3
https://minecraftfpv.com/track/1EC77A23F05E61AE85462B1AE563A551
https://minecraftfpv.com/track/1EC752BA87BC65E692DE8F43CBD6AD2C
https://minecraftfpv.com/track/1EB426026B2A6F458705F135F65B5917
https://minecraftfpv.com/track/1EB9221753976DD78509ED68055741F2
https://minecraftfpv.com/track/1EC6D6ED8F3F675D968887369A9CD14B
https://minecraftfpv.com/track/1EC6D69E4A336EDC968887369A9CD14B
https://minecraftfpv.com/track/1EC6E52E784B6407AD89F983A662A9D5
https://minecraftfpv.com/track/1EC7E94DF1FB67F086619D0FC10E4FAB
https://minecraftfpv.com/track/1EC712EC65ED6228B5287D00EBAB6196
https://minecraftfpv.com/track/1EC74C57F354673692DE8F43CBD6AD2C
https://minecraftfpv.com/track/1EC75300F319640892DE8F43CBD6AD2C
https://minecraftfpv.com/track/1EC77A116AD96FAE85462B1AE563A551
https://minecraftfpv.com/track/1EC6CFC1DBFF6367834B035C4805D8E1
https://minecraftfpv.com/track/1EBB7CBE7EE969FA9C54EF5C2CF3932A
https://minecraftfpv.com/track/1EC7494EEB426DA392DE8F43CBD6AD2C
https://minecraftfpv.com/track/1EB425D6668369058705F135F65B5917
https://minecraftfpv.com/track/1EC6A38F5EC96C8EBE585FD3A4E0DBA6
https://minecraftfpv.com/track/1EC935B33162692FB99B6773E417E197""".split()

positions = ""

driver_path = r'C:\Users\Revvilo\Desktop\chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
for URL in URLs:
    print("Getting URL: " + URL, end='')
    driver.get(URL)
    try:
        elem = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "sub-title"))
        )
    finally:
        pos = driver.find_element_by_class_name("sub-title").text[11:-1]
        name = driver.find_element(By.CLASS_NAME, 'title').text.split()[0]
        print(" -- Got: {} at {}".format(name,pos))
        positions += "\n{}:{}:{}".format(name,name[0],pos)
print(positions)
input("Execution Complete")
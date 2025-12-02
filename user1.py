import requests
import json
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def main():
    retry = 3
    for attempts in range(1, retry + 1):
        try:
            url = "https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download"
            file_path = "data.csv"
            response = requests.get(url)

            with open(file_path, "wb") as f:  #writes the google drive url content in csv file
                f.write(response.content)

            if not file_path.endswith(".csv"):
                raise ValueError("incorrect file type!!")


            df = pd.read_csv("data.csv")
            df = df.rename(columns={"User Id": "Employee ID", "Phone": "Phone Number"})
            df = df[["Employee ID", "First Name", "Last Name", "Email",     
                     "Job Title", "Phone Number", "Date of birth"]]

            file_path2 = "output.csv"
            df.to_csv(file_path2)
            logging.info("\n%s",df)           
            return df,"data.csv"
            break


            #error handling
        except requests.exceptions.HTTPError as e:
            logging.error("Sorry! file Download failed:", e)

        except Exception as e:
            logging.error("Sorry Error!",e)

        if attempts == retry:
            logging.error("Sorry Maximum limit reached!")
        else:
            logging.error("Retrying.....")


if __name__ == "__main__":
    main()

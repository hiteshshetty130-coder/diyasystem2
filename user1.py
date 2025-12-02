import requests
import json
import pandas as pd


def main():
    retry = 3
    for attempts in range(1, retry + 1):
        try:
            url = "https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download"
            file_path = "data.csv"
            response = requests.get(url)

            with open(file_path, "wb") as f:
                f.write(response.content)

            if not file_path.endswith(".csv"):
                raise ValueError("incorrect file type!!")


            df = pd.read_csv("data.csv")
            df = df.rename(columns={"User Id": "Employee ID", "Phone": "Phone Number"})
            df = df[["Employee ID", "First Name", "Last Name", "Email",
                     "Job Title", "Phone Number", "Date of birth"]]

            file_path2 = "output.csv"
            df.to_csv(file_path2)
            print(df)
            return df,"data.csv"
            break

        except requests.exceptions.HTTPError as e:
            print("Sorry! file Download failed:", e)

        except Exception as e:
            print("Sorry Error!",e)

        if attempts == retry:
            print("Sorry Maximum limit reached!")
        else:
            print("Retrying.....")


if __name__ == "__main__":
    main()

import unittest
from unittest.mock import patch,Mock
from user1 import main
import os
import pandas as pd


class TestCsvFileDownload(unittest.TestCase):
    #Test case 1: verify csv file download
    @patch("user1.requests.get")
    def test_main1(self,mock_get):
        mock_data=b"User Id,First Name,Last Name,Sex,Email,Phone,Date of birth,Job Title\n1,8717bbf45cCDbEe,Shelia,Mahoney,Male,pwarner@example.org,857.139.8239,2014-01-27,Probation officer"
        mock_response=Mock()
        mock_response.status_code=200
        mock_response.content=mock_data
        mock_get.return_value=mock_response

        df,file_path=main()

        self.assertIsNotNone(file_path)
        self.assertTrue(os.path.exists(file_path))

    @patch("user1.requests.get")
    #Test case 2: validate csv file extraction
    def test_main2(self,mock_get):
        mock_data = b"User Id,First Name,Last Name,Sex,Email,Phone,Date of birth,Job Title\n1,8717bbf45cCDbEe,Shelia,Mahoney,Male,pwarner@example.org,857.139.8239,2014-01-27,Probation officer"
        mock_response=Mock()
        mock_response.status_code=200
        mock_response.content=mock_data
        mock_get.return_value=mock_response

        df,file_path=main()

        self.assertEqual(len(file_path),8)
        self.assertTrue(file_path.endswith(".csv"))

    @patch("user1.requests.get")
    #test case 3:verify file type and format
    def test_main3(self,mock_get):
        mock_data = b"User Id,First Name,Last Name,Sex,Email,Phone,Date of birth,Job Title\n1,8717bbf45cCDbEe,Shelia,Mahoney,Male,pwarner@example.org,857.139.8239,2014-01-27,Probation officer"
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = mock_data
        mock_get.return_value = mock_response

        df,file_path=main()
        file_path1="data.csv"

        self.assertTrue(file_path.endswith("data.csv"))
        self.assertTrue(os.path.exists(file_path))

        try:
            df=pd.read_csv(file_path1)
            self.assertIsInstance(df,pd.DataFrame)

        except Exception as e:
            self.fail("Exception Occurred ",e)

    @patch("user1.requests.get")
    #test case 4:validate data structure
    def test_main4(self,mock_get):
        mock_data = b"User Id,First Name,Last Name,Sex,Email,Phone,Date of birth,Job Title\n1,8717bbf45cCDbEe,Shelia,Mahoney,Male,pwarner@example.org,857.139.8239,2014-01-27,Probation officer"
        mock_response=Mock()
        mock_response.content=mock_data
        mock_get.return_value=mock_response

        df,file_path=main()

        expected_col=["Employee ID", "First Name", "Last Name", "Email",
                     "Job Title", "Phone Number", "Date of birth"]

        for col in expected_col:
            self.assertIn(col,df.columns)

    @patch("user1.requests.get")
    #test case 5:handle missing and invalid data
    def test_main5(self, mock_get):
        mock_data = b"User Id,First Name,Last Name,Sex,Email,Phone,Date of birth,Job Title\n1,8717bbf45cCDbEe,Shelia,Mahoney,Male,pwarner@example.org,857.139.8239,2014-01-27,Probation officer"
        mock_response = Mock()
        mock_response.content = mock_data
        mock_get.return_value = mock_response

        df, file_path = main()

        assert df.isnull().any().any() == False , "No Null Values Exist"

        for Email in df["Email"]:
            self.assertIn("@",Email,"Invalid Email")




if __name__=="__main__":
    unittest.main()


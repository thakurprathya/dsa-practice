import pandas as pd
import sys

def pick_random_problem(file_path):
    """
    Reads an Excel (.xlsx) or CSV (.csv) file, filters for unsolved problems,
    and picks a random one to display.
    """
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path, engine='openpyxl')
        else:
            print(f"Error: Unsupported file format. Please use a '.csv' or '.xlsx' file.")
            return

        unsolved_problems = df[df['Solved'].isna()]
        if unsolved_problems.empty:
            print("🎉 Congratulations! You have solved all the problems in the sheet.")
            return

        random_problem = unsolved_problems.sample(n=1)

        problem_name = random_problem['Problem Name'].iloc[0]
        # difficulty = random_problem['Difficulty'].iloc[0]
        link = random_problem['Link'].iloc[0]

        print("--- Your Random Problem ---")
        print(f"\nProblem: {problem_name}")
        # print(f"Difficulty: {difficulty}")
        print(f"Link: {link}\n")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except KeyError as e:
        print(f"Error: A required column is missing from your file. Missing column: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python your_script_name.py <path_to_your_sheet.xlsx_or_csv>")
    else:
        sheet_file = sys.argv[1]
        pick_random_problem(sheet_file)
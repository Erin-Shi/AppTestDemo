# run_test.py
import subprocess
from driver.driver_manager import DriverManager

def run_behave_test():
    """Run Behave BDD tests (execute scenarios in the features directory)"""
    try:
        # Execute behave command: --no-capture shows print logs; --tags filters scenarios (optional)
        result = subprocess.run(
            ["behave", "features/", "--no-capture"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("Behave tests executed successfully:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Behave tests execution failed:")
        print(e.stderr)
    finally:
        # Shut down the driver regardless of success or failure
        DriverManager.quit_driver()

def run_pytest_test():
    """Run Pytest tests (execute cases in the tests directory)"""
    try:
        # Execute pytest command: -v shows detailed logs; -s shows print output
        result = subprocess.run(
            ["pytest", "tests/", "-v", "-s"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("Pytest tests executed successfully:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Pytest tests execution failed:")
        print(e.stderr)
    finally:
        DriverManager.quit_driver()

if __name__ == "__main__":
    # Select test type to execute (default: Behave BDD tests)
    print("1. Run Behave BDD tests")
    print("2. Run Pytest tests")
    choice = input("Please enter your choice (1/2): ")

    if choice == "1":
        run_behave_test()
    elif choice == "2":
        run_pytest_test()
    else:
        print("Invalid input, running Behave BDD tests by default")
        run_behave_test()
import pandas as pd
import numpy as np

df = pd.read_csv('NYPD_Shooting_Incident_Data__Historic_.csv')

def main():

    df["SAME_SEX_SHOOTING"] = np.where(df["PERP_SEX"] == df["VIC_SEX"], 'True', 'False')
    sorted_columns = sorted(df.columns)

    print('\nSorted Columns:\n')

    for col in sorted_columns:
        print(col)

    df.to_csv("Shootings_Report.csv", index=False)
    
    # print(df)
    print('\nRows: ' + str(len(df.index)))
    print('Columns: ' + str(len(df.columns)))
    print("\nFinished\n")
    print('Updated DataFrame (new column): Shootings_Report.csv')
    print('New column titled: SAME_SEX_SHOOTING\n')

if __name__ == '__main__':
    exit(main())

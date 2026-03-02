import datetime
import uuid
import numpy as np
import pandas as pd
import sqlalchemy as db


def main():
    rorFp = "/home/ubuntu/data/ror/v1.70-2025-08-26-ror-data.csv"
    df = pd.read_csv(rorFp, sep=',', dtype=str, na_filter=False)

    # print(df)

    # Selecting and renaming columns to match DB column names
    df_ror = df[["id", "name", "country.country_code", "country.country_name", "addresses[0].geonames_city.name", "status"]]
    df_ror = df.rename(columns={"id": 'ror_id', "name": "default_name", "country.country_code": 'country_code', "country.country_name": "country_name", 
                                "addresses[0].geonames_city.name": "city", "status": "is_current"})
    # SAS verification true if approved, otherwise false
    df_ror['is_current'] = np.where(df_ror['is_current'] == "active", True, False)

    # Engine for connection
    user = input("Enter DB user: ")
    password = input("Enter DB password: ")
    engine = db.create_engine(f'postgresql+psycopg2://{user}:{password}@localhost:5441/esbs')

    # Tables to use
    metadata = db.MetaData()
    organisations = db.Table('organisations', metadata, autoload_with=engine)

    with engine.connect() as conn:
        for index, row in df_ror.iterrows():
            # Checking if ror id present in DB
            stmt_ror = db.select(organisations.c.ror_id).where(organisations.c.ror_id == row["ror_id"])

            # All converts a CursorResult object into a Python Sequence (tuples)
            res_ror = conn.execute(stmt_ror).all()

            if (len(res_ror) == 0): # Ror ID not present in DB, adding organisation
                # print(row)

                # Inserting Organisation
                row_dict = row.to_dict()
                row_dict["id"] = uuid.uuid4()
                row_dict["created_on"] = datetime.datetime.utcnow()
                conn.execute(organisations.insert(), row_dict)
                conn.commit()
    print("Done!")



if __name__ == "__main__":
    main()
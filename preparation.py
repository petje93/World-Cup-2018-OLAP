from sqlalchemy import create_engine
from cubes.tutorial.sql import create_table_from_csv

engine = create_engine('sqlite:///world_cup.sqlite')

print("...wait (about 3 minutes)")

create_table_from_csv(engine,
                      "WC18.csv",
                      table_name="players",
                      fields=[
                            ("name", "string"),
                            ("nat_team", "string"),
                            ("club", "string"),
                            ("league", "string"),
                            ("pos", "string"),
                            ("role", "string"),
                            ("age_gr", "string"),
                            ("age_ex", "string"),
                            ("matches", "integer"),
                            ("goals", "integer"),
                            ("assists", "integer"),
                            ("ycards", "integer"),
                            ("rcards", "integer"),
                            ("minutes", "integer"),
                            ("n-caps", "integer"),
                            ("n-goals", "integer")],
                      create_id=True
                  )

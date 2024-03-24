table_query = {"game":f"""CREATE TABLE game (
                    game_id SERIAL PRIMARY KEY,
                    name VARCHAR(60) NOT NULL);""",
               "item": f"""CREATE TABLE item(
                    item_id SERIAL PRIMARY KEY,
                    name VARCHAR(60) NOT NULL,
                    game_id INT NOT NULL,
                    FOREIGN KEY(game_id) REFERENCES game(game_id)
                    );""",
               "recipe": f"""CREATE TABLE recipe(
                    recipe_id SERIAL PRIMARY KEY,
                    name VARCHAR(60) NOT NULL,
                    item_id INT NOT NULL,
                    item_quantity INT NOT NULL,
                    FOREIGN KEY (item_id) REFERENCES item(item_id)
                    );""",
               "components": f"""CREATE TABLE components(
                    component_id SERIAL PRIMARY KEY,
                    name VARCHAR(60) NOT NULL,
                    component_quantity INT,
                    item_id INT,
                    FOREIGN KEY (item_id) REFERENCES item(item_id)
                    );""",
               "recollection_mission": f"""CREATE TABLE recollection_mission(
                    recollection_mission_id SERIAL PRIMARY KEY,
                    mission_name VARCHAR(60) NOT NULL,
                    game_id INT,
                    FOREIGN KEY(game_id) REFERENCES game(game_id)
                    );"""
               }
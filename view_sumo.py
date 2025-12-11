# view_sumo.py
# Vizualizează o singură zi de trafic în SUMO-GUI (fără RL, fără mutație).

from routerl import TrafficEnvironment


def main():
    env_params = {
        "agent_parameters": {
            "num_agents": 50,
            "new_machines_after_mutation": 0, 
            "human_parameters": {
                "model": "culo",
            },
            "machine_parameters": {
                "behavior": "malicious",
            },
        },
        "simulator_parameters": {
            "network_name": "bucharest",
            "sumo_type": "sumo-gui", 
            "simulation_timesteps": 180,
        },
        "path_generation_parameters": {
            "number_of_paths": 2,
            "beta": -5,
        },
        "plotter_parameters": {
            "records_folder": "training_records",
            "plots_folder": "plots",
            "phases": [0, 1],
            "smooth_by": 10,
        },
    }

    env = TrafficEnvironment(seed=42, **env_params)

    print("Number of total agents:", len(env.all_agents))
    print("Number of human agents:", len(env.human_agents))
    print("Number of machine agents:", len(env.machine_agents))

    env.start()  
    env.step()      
    print("Simulation finished – you can inspect it in SUMO-GUI.")
    input("Apasă Enter ca să închizi SUMO...")
    env.stop_simulation()


if __name__ == "__main__":
    main()
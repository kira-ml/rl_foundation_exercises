NUM_STATES = 10



def run_state_loop() -> None:
    for i in range(NUM_STATES):
        print(f"State {i}")

if NUM_STATES <= 0:
    raise ValueError("NUM_STATES must be positive.")



if __name__ == "__main__":
    run_state_loop()



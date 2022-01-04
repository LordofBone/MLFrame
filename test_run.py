from functions.build_and_display import BuildDisplay

if __name__ == "__main__":
    test_run = BuildDisplay(show_image=True)
    test_run.run_neural_transfer()
    test_run.display_to_ink()

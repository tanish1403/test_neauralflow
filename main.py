import tensorflow as tf
import tensorflow

class neuralflow_model:
    def __init__(self, model_file="demo_model.txt", model_saved="model.h5"):
        self.model_file = model_file
        self.model_saved = model_saved

    def check_tensorflow(self):
        """
        Checks if tensorflow is installed.

        Prints the version of tensorflow if it is installed, otherwise
        prints a message asking the user to install it.

        This function does not have any parameters.

        This function does not return anything.
        """
        try:
            # Try to print the version of tensorflow
            print("tensorflow_info", tensorflow.version.VERSION)
        except:
            # If tensorflow is not installed, print a message asking the user to install it
            print("Please install tensorflow")

    def get_model_from_file(self):
        """
        Load a saved Keras model from a file.

        Returns:
            model (tf.keras.Model): The loaded Keras model.
        """
        # Load the model from the file specified in the constructor
        # The model is not compiled, as it might be compiled later
        model = tf.keras.models.load_model(self.model_saved, compile=False)
        
        return model
        return
    def get_model_from_var(self):
        """
        Reads the model from a file and returns it as a Keras model object.
        
        Returns:
            model (tf.keras.Model): The model read from the file.
        """
        
        # Open the file containing the model definition
        with open(self.model_file) as f:
            # Read the contents of the file
            demo_model = f.read()

        # Create a dictionary to serve as the namespace for exec()
        # This dictionary will hold the model object after it is defined in the file
        namespace = {}

        # Execute the code in the file in the namespace
        # The model object defined in the file will be added to the namespace
        exec(demo_model, globals(), namespace)

        # Now you can access 'model' from the namespace dictionary
        # This is the model object read from the file
        model = namespace['model']

        return model

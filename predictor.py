import argparse
import pickle
import numpy as np

def artist_predictor():
	"""
	Using a prepared Pickle model, this script prompts the user for text input and assesses the probability that it was sung by David Bowie or Tina Turner.
	"""
	
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('-f', '--file', help='load lyrics via txt file')
	group.add_argument('-l', '--line', help='load lyrics via line')

	args = parser.parse_args()

	with open("artist_predictor_bayes.pkl", "rb") as artist_predictor:
		model = pickle.load(artist_predictor)

	if args.file:
		with open(args.file, 'r') as lyrics_file:
			lyrics = [lyrics_file.read()]

	if args.line:
		lyrics = [args.line]

	artist_predicted = np.array2string(model.predict(lyrics))
	artist_probability = int(100*max(max(model.predict_proba(lyrics))))

	print("There is a " + str(artist_probability) + "% chance that " + artist_predicted[2:-2] + " was the artist.")

if __name__ == "__main__":
	artist_predictor()
import json

if __name__ == '__main__':
	gold_file = "data/ve/test.json"
	pred_file = "snap/ve/ve_results/test_predict.json"

	gold = json.load(open(gold_file))
	test = json.load(open(pred_file))

	id_to_gold = {}
	for elem in gold:
		#print(list(elem["label"].keys()))
		id_to_gold[elem["question_id"]] = list(elem["label"].keys())[0]

	count = 0
	for elem in test:
		pred_label = elem["answer"]
		if pred_label == id_to_gold[elem["question_id"]]:
			count += 1 

	print(float(count)/len(gold))

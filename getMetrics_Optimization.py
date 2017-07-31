import os
import argparse

def getMetrics(input_path,conceptFreq_max,output_path):
	"""input: input_path = the path to where all the info files are with all the metrics for each run in the range
				conceptFreq_max = the max conceptFreq used in the range
				output_path = where the output files should go
		Output: a file for each ontology with the a line for maximizing precision, recall, and F-measure """
	
	##For each file in the input path with evaluation metric information: find the conceptFreq that maximizes precision, recall, and F-measure separately
	for file in os.listdir(input_path):
		if '_info.txt' in file: #files of interest that have the evaluation metrics
			print 'ontology:', file
			with open(input_path+file,'r') as f:
				#Initialize a vector for precision, recall, and F-measure the size of the range of ConceptFreq
				#the index is the concept frequency
				precision_vector = [0]*conceptFreq_max 
				recall_vector = [0]*conceptFreq_max
				Fmeasure_vector = [0]*conceptFreq_max

				#Get the ontology, conceptFreq, precision, recall, and F-measure out of the file
				for line in f:
					if line.startswith('cm-craft-'): #ontology name from the file name
						ontology = line.replace('\n','')
						# print 'ontology', ontology
						conceptFreq = int(line.split('.')[-2]) #concept frequency for each document
					else: #evaulation metrics

						##Precision information
						precision_spot = line.split('\t')[4]
						#check to make sure we got precision (P=) otherwise error
						if precision_spot.split('=')[0] != 'P': 
							print 'precision error'
						else: 
							precision_vector[conceptFreq-1] = float(precision_spot.split('=')[-1]) #index is the conceptfrequency
						
						##Recall information
						recall_spot = line.split('\t')[5]
						#check to make sure we got recall (R=) otherwise error
						if recall_spot.split('=')[0] != 'R': 
							print 'recall error'
						else:
							recall_vector[conceptFreq-1] = float(recall_spot.split('=')[-1]) #index is the conceptfrequency
						
						##F-measure information
						Fmeasure_spot = line.split('\t')[6]
						#check to make sure we got F-measure (F=) othwerise error
						if Fmeasure_spot.split('=')[0] != 'F': 
							print 'recall error'
						else:
							Fmeasure_vector[conceptFreq-1] = float(Fmeasure_spot.split('=')[-1]) #index is the conceptfrequency

				#Find the index of the max precision, recall, and F-measure = conceptFreq
				maxP_ConceptFreq = precision_vector.index(max(precision_vector))+1
				maxR_ConceptFreq = recall_vector.index(max(recall_vector))+1
				maxF_ConceptFreq = Fmeasure_vector.index(max(Fmeasure_vector))+1

				##Output:
				ontology_output = open(output_path+'%s_maximization_info.txt' %ontology,'a+')
				ontology_output.write('%s\t%s\t%s\t%s\t%s\n' %('Maximum', 'Max concept frequency', 'Precision', 'Recall', 'F-measure'))
				##Precision
				ontology_output.write('%s\t%s\t%s\t%s\t%s\n' %('Max Precision',maxP_ConceptFreq, precision_vector[maxP_ConceptFreq-1], recall_vector[maxP_ConceptFreq-1], Fmeasure_vector[maxP_ConceptFreq-1]))
				##Recall
				ontology_output.write('%s\t%s\t%s\t%s\t%s\n' %('Max Recall',maxR_ConceptFreq, precision_vector[maxR_ConceptFreq-1], recall_vector[maxR_ConceptFreq-1], Fmeasure_vector[maxR_ConceptFreq-1])) 
				##F-measure
				ontology_output.write('%s\t%s\t%s\t%s\t%s\n' %('Max F-measure',maxF_ConceptFreq, precision_vector[maxF_ConceptFreq-1], recall_vector[maxF_ConceptFreq-1], Fmeasure_vector[maxF_ConceptFreq-1])) 


#Run the main program using argparse
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('input_path',type=str,help='Input a path to where all the evaulation metrics are for each run of ConceptMapper over the range of Concept Frequencies. The files contain "info" in the name')
	parser.add_argument('conceptFreq_max',type=int,help='Input the max concept frequency used')
	parser.add_argument('output_path',type=str,help='Input a path to where the output files should go')
	args = parser.parse_args()
	getMetrics(args.input_path,args.conceptFreq_max,args.output_path)

# input_path = '/Users/maylaboguslav/Documents/Larry_Kevin_rotation/Distribution_info/LeqConceptFreq/'
# conceptFreq_max = 50
# output_path = '/Users/maylaboguslav/Documents/Larry_Kevin_rotation/Distribution_info/LeqConceptFreq/'
# getMetrics(input_path,conceptFreq_max,output_path)







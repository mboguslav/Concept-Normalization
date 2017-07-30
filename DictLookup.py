import enchant
import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import argparse


#The English dictionary
d = enchant.Dict("en_US")

def DictLookup(input_path, output_path):
	'''input: dictionary file from the output of running concept mapper, 
		output: list of terms that are in the english dictionary - canonical form or synonyms '''

	#Initialize variables
	Problem_terms = {} #dictionary name to problem terms
	total_words_all = [] #all the counts of the total number of single words
	total_english_words_all = [] #all the counts of the total number of English words
	labels = [] #name of ontology dictionary

	#For each dictionary file in the input_path: find the single words and check if they are in the English dictionary
	for file in os.listdir(input_path): 
		if 'cmDict-' in file: #Dictionary file names (cm = ConceptMapper)
			total_words = 0 #count of how many single words
			total_english_words = 0 #count of how many English words

			#Output file
			Variants_InEnDict = open(output_path +'%s' %(str(file).split('.xml')[0]), 'a+')
			Variants_InEnDict.write('%s\t%s\t%s\n' %('Ontology Term', 'Concept', 'Variant'))
			
			#open the dictionary file and check if the single words are in the English dictionary
			with open(input_path+file,'r'):
				tree = ET.parse(input_path+file) #tree = token id, canonical, variant base (first one is same as canonical)
				root = tree.getroot() #synonyms
				for child in root: #for each ontology term
					ont_term = str(child.attrib['id']).split('obo/')[-1] #ontology id

					for i,variant in enumerate(child.iter('variant')): #for each variant (synonym)
						if ' ' not in variant.attrib['base'] and '/' not in variant.attrib['base']: #only single words so no spaces in between words
							total_words += 1 #update the total number of single words
							if i > 0: #synonyms since the first variant is the same as the canonical form
								if d.check(variant.attrib['base']) == True: #check if the word is in the English dictionary
									total_english_words += 1 #update the total number of English words
									if i == 0: #if the variant is just the canonical form 
										Variants_InEnDict.write('%s\t%s\t%s\t%s\n' %('canonical',ont_term, child.attrib['canonical'], variant.attrib['base'])) #write canonical so we know 
									else:
										Variants_InEnDict.write('%s\t%s\t%s\n' %(ont_term, child.attrib['canonical'], variant.attrib['base'])) #otherwise it is not the canonical form and synonyms

							else: #canonical form only
								if d.check(child.attrib['canonical']) == True: #check if the word is in the English dictionary
									total_english_words += 1 #update the total number of English words
									Variants_InEnDict.write('%s\t%s\t%s\t%s\n' %('canonical',ont_term, child.attrib['canonical'], variant.attrib['base'])) #write canonical so we know 
						else: #mutliwords
							pass
			labels += [file.split('-')[-1].split('.')[0]] #name of ontology dictionary
			total_words_all += [total_words] #all the counts of the total number of single words
			total_english_words_all += [total_english_words] #all the counts of the total number of English words

	# print labels
	# print total_words_all
	# print total_english_words_all
	Fraction_english_words = [float(total_english_words_all[f])/float(total_words_all[f]) for f in range(0,len(labels))] #the fraction of the number of english words over the number of total single words for all ontologies
	# print Fraction_english_words

	#Create a histogram of Fraction_english_words for all ontologies
	plt.bar(range(len(Fraction_english_words)), Fraction_english_words, align='center')
	plt.xticks(range(len(Fraction_english_words)), labels, size='small')
	plt.xlabel('Ontology')
	plt.ylabel('# English words/# Total words')	# plt.set_xticks(labels[:-1])
	# plt.show()
	plt.savefig(output_path+'Ontology_hardness.pdf')


#add def main() that inputs the path of where the files are


## Run the main program and print out the time it takes to run it
if __name__ == '__main__':
	### Argparse - parse arguments in command line: need training set, optional: minPrecision, minRecall, and test_set
	parser = argparse.ArgumentParser()
	parser.add_argument('input_path',type=str,help='Input the path to the ontology dictionary files that start with "cmDict"')
	parser.add_argument('output_path',type=str,help='Input the path to where you would like the output')
	args = parser.parse_args()
	DictLookup(args.input_path, args.output_path)



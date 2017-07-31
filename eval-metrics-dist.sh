#!/bin/bash
file="cm-craft-"
end="_info.txt"
for i in $(ls); do
	for ontology in NCBITAXON PR SO chebi cl go_bp go_cc go_mf; do
	#	echo "$file$ontology"
		filename=$file$ontology
		if [[ $i =~ $filename.* ]]; then
			echo $i >> $ontology$end
			tail -n 2 $i | head -n 1 >> $ontology$end
		fi
	done
done

package edu.ucdenver.ccp.nlp.pipelines.evaluation.craft.conceptmapper;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class RunAllOntologiesConceptMapper {
	public static void main(String[] args) {
		String[] parameters_GO_CC = new String[] { "-i", "31", "-d", "/tmp/cm-evals/cm-dicts/", "-o",
				"/tmp/cm-evals/eval-output", "-c", "true", "-m", "GO_CC", "-t", "GOCC", "-p", "cm-craft-go_cc" };
		String[] parameters_CHEBI = new String[] { "-i", "189", "-d", "/tmp/cm-evals/cm-dicts/", "-o",
				"/tmp/cm-evals/eval-output", "-c", "true", "-m", "CHEBI", "-t", "CHEBI", "-p", "cm-craft-chebi" };
		String[] parameters_PR = new String[] { "-i", "286", "-d", "/tmp/cm-evals/cm-dicts/", "-o",
				"/tmp/cm-evals/eval-output", "-c", "true", "-m", "PR", "-t", "PR", "-p", "cm-craft-PR" };
		String[] parameters_GO_BP = new String[] { "-i", "47", "-d", "/tmp/cm-evals/cm-dicts/", "-o",
				"/tmp/cm-evals/eval-output", "-c", "true", "-m", "GO_BP", "-t", "GOBP", "-p", "cm-craft-go_bp" };
		String[] parameters_CL = new String[] { "-i", "143", "-d", "/tmp/cm-evals/cm-dicts/", "-o",
				"/tmp/cm-evals/eval-output", "-c", "true", "-m", "CL", "-t", "CL", "-p", "cm-craft-cl" };
		String[] parameters_NCBI_TAXON = new String[] { "-i", "279", "-d", "/tmp/cm-evals/cm-dicts/", "-o",
				"/tmp/cm-evals/eval-output", "-c", "true", "-m", "NCBI_TAXON", "-t", "NCBITAXON", "-p",
				"cm-craft-NCBITAXON" };
		String[] parameters_GO_MF = new String[] { "-i", "111", "-d", "/tmp/cm-evals/cm-dicts/", "-o",
				"/tmp/cm-evals/eval-output", "-c", "true", "-m", "GO_MF", "-t", "GOMF", "-p", "cm-craft-go_mf" };
		String[] parameters_SO = new String[] { "-i", "191", "-d", "/tmp/cm-evals/cm-dicts/", "-o",
				"/tmp/cm-evals/eval-output", "-c", "true", "-m", "SO", "-t", "SO", "-p", "cm-craft-SO" };

		List<String[]> allParameters = new ArrayList<String[]>();
		allParameters.add(parameters_GO_CC);
		allParameters.add(parameters_CHEBI);
		allParameters.add(parameters_PR);
		allParameters.add(parameters_GO_BP);
		allParameters.add(parameters_CL);
		allParameters.add(parameters_NCBI_TAXON);
		allParameters.add(parameters_GO_MF);
		allParameters.add(parameters_SO);

		for (String[] arguments : allParameters) {
			for (int conceptFreq = 0; conceptFreq <= 100; conceptFreq++) {
				String[] argsWithConceptFreq = Arrays.copyOf(arguments, arguments.length + 2);
				argsWithConceptFreq[argsWithConceptFreq.length - 2] = "-f";
				argsWithConceptFreq[argsWithConceptFreq.length - 1] = Integer.toString(conceptFreq);
				argsWithConceptFreq[argsWithConceptFreq.length - 3] = arguments[arguments.length - 1] + "."
						+ Integer.toString(conceptFreq);

				System.out.println("PARAMETERS: " + Arrays.toString(argsWithConceptFreq));
				new MaylaCraftConceptMapperEvaluatorMain().startProcessing(argsWithConceptFreq);
			}
		}
	}
}

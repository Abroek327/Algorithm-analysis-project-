.PHONY: run

clean:
	rm testing_script.txt
	rm SampleOutput_1.0.txt
run:
	python3 testing_script_generator.py
	python3 parlay_testing_version.py < testing_script.txt > ZampleOutput_3.0.txt
	python3 results.py

runBF:
	python3 ts_genBF.py
	python3 parlayBFonly.py < testing_scriptBF.txt > ZampleOutput_4.0.txt

test:

	number=1 ; while [[ $$number -le 500 ]] ; do \
        python3 testing_script_generator.py ; \
	python3 parlay_testing_version.py < testing_script.txt >> ZampleOutput_3.0.txt ; \
        ((number = number + 1)) ; \
	done


testBF:
	number=1 ; while [[ $$number -le 300 ]] ; do \
        python3 ts_genBF.py ; \
	python3 parlayBFonly.py < testing_scriptBF.txt >> ZampleOutput_4.0.txt ; \
        ((number = number + 1)) ; \
	done

fetchData:
	python3 test_data_reader.py < ZampleOutput_3.0.txt

fetchDatag10+:
	python3 test_data_reader_g10+.py < ZampleOutput_3.0.txt

fetchDatag10+BF:
	python3 test_data_reader_g10+.py < ZampleOutput_4.0.txt
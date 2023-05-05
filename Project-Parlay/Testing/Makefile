.PHONY: run

clean:
	rm testing_script.txt
	rm SampleOutput_1.0.txt
run:
	python3 testing_script_generator.py
	python3 parlay_testing_version.py < testing_script.txt > ZampleOutput_1.0.txt

test:

	number=1 ; while [[ $$number -le 1000 ]] ; do \
        python3 testing_script_generator.py ; \
	python3 parlay_testing_version.py < testing_script.txt >> ZampleOutput_1.0.txt ; \
        ((number = number + 1)) ; \
	done

fetchData:
	python3 test_data_reader.py < ZampleOutput_1.0.txt
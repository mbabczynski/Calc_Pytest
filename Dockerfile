FROM python: 3.10.5
MAINTAINER babczynski@o2.pl
COPY . /python-test-calculator
WORKDIR /python-test-calculator
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null

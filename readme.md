# An automated approach to nuke non-compliant resources in a sandbox account (Proof of Concept)

## Description
The idea here is use a python script to retrive the list of compliant resources from a AWS Config rule
and use [aws-nuke](https://github.com/rebuy-de/aws-nuke) to remove everything that doesnt match
the resources got it.
The script can be run from Jenkins or similiar tools and an schedule way (probably daily)
and clean up automatically the non-compliant resources.

## Usage
1. Clone this repo
```
git clone https://github.com/egarbi/aws-non-compliant-remover
```
2. Dependencies will be managed by pipenv
```
pip install pipenv
```
3. Install python dependencies
```
pipenv install
```
4. Run the config generator, will be used as an input of aws-nuke
```
python3 ./generate_aws-nuke_config.py
```
5. Remove all resources except those stated as in compliant by an AWS Config rule.

To see how to have aws-nuke running see [here](https://github.com/rebuy-de/aws-nuke#install)
```
./aws-nuke -c config.yaml
```

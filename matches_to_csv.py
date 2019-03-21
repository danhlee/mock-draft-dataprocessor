import csv, json, sys
import os.path
#if you are not using utf-8 files, remove the next line

#check if you pass the input file and output file

directory = './matches/'
for jsonFile in os.listdir(directory):
  

  inputFile = open( directory + jsonFile )
  if os.path.isfile('matches.csv'):
    outputFile = open('matches.csv','a', newline='')
  else:
    outputFile = open('matches.csv','w', newline='')

  csvWriter = csv.writer(outputFile)
  matchesObject = json.load(inputFile)
  matchesArray = matchesObject['matches']

  for match in matchesArray:
    participants = match['participants']
    teams = match['teams']
    winner = ''
    if teams[0]['win'] == 'Win':
      winner = '100'
    else:
      winner = '200'

    #match_tuple = ''
    championsArray = []
    for participant in participants:
      #match_tuple += ( str(participant['championId']) + ',')
      
      lane = participant['timeline']['lane']
      role = participant['timeline']['role']
      team = participant['teamId']
      

      championsArray.append(participant['championId'])

    #match_tuple += winner
    championsArray.append(winner)
    csvWriter.writerow(championsArray)
  inputFile.close()
  outputFile.close()
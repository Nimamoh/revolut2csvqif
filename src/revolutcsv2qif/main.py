import argparse
import csv

import quiffen

def main():
    parser = argparse.ArgumentParser('Transformer un fichier csv de revout en qif')

    parser.add_argument('csv', type=str, help='Chemin vers le csv')

    args = parser.parse_args()

    # Qif
    qif = quiffen.Qif()
    acc = quiffen.Account(name='Personal Bank Account', desc='My personal bank account with Barclays.')
    qif.add_account(acc)
    #

    with open(args.csv, mode='r') as fichier:
        reader = csv.DictReader(fichier, skipinitialspace=True)
        # header = next(reader)
        for line in reader:
            tr = quiffen.Transaction(
                date = line["Completed Date"] or line["Started Date"],
                amount=line["Amount"],
                memo=line["Description"],
            )
            acc.add_transaction(tr, header='Bank')
    
    qif.to_qif('revolut.qif')

if __name__ == "__main__":
    main()
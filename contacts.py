import settings
import click
import json
from hubspot3.contacts import ContactsClient

contacts_cli = click.Group()

@contacts_cli.command()
@click.option('--file', type=click.Path(exists=True), help='Path to the file contains a list vids to be deleted.')
@click.option('--vid', help='A single contact to be deleted')
def delete(file, vid):
    if file != None:
        with open(file, 'r') as f:
            vids = f.readlines()

        vids = [x.strip() for x in vids]
        click.confirm('%d contacts will be deleted, please confirm to delete the contacts' % (len(vids)), abort=True)
        for vid in vids:
            deleteContact(vid)

    if vid != None:
        deleteContact(vid)

def deleteContact(vid):
    client = ContactsClient(api_key=settings.API_KEY)
    click.echo('Deleting: %s' % (vid))
    result = client.delete_a_contact(vid)
    click.echo(json.dumps(result))


@contacts_cli.command()
@click.option('--email', help='Search contacts by email')
@click.option('--vid', help='Search contacts by vid')
def search(email, vid):
    contacts_client = ContactsClient(api_key=settings.API_KEY)

    if email != None:
        contact = contacts_client.get_contact_by_email(email)
        print(contact)

    if vid != None:
        contact = contacts_client.get_contact_by_id(vid)
        click.echo(json.dumps(contact))


if __name__ == '__main__':
    contacts_cli()

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from james_bond_assistant.james_logic import secure_main, get_help, clean, boot_logo, edit_note, delete_note, add_address, add_birthday, add_email, add_phone, edit_phone, remove_phone, save, load, note_file, find_phone, find_record, find_tag, uncoming_birthdays, create_contact, create_note, show_contacts, show_notes, delete_contact
import getpass
from abc import ABC, abstractmethod

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"


exit_list = ('exit', 'quit', 'end')
help_comm = ('help','?')

command_menu = WordCompleter(['create-note', 'show-notes', 'save-data', 'load-data',
                              'quit', 'exit', 'find-tag', 'create-contact', 'show-contacts', 'find-record', 'add-phone',
                              'find-phone', 'delete-contact', 'remove-phone','add-email', 'add-address', 'add-birthday', 
                              'edit-phone', 'uncoming-birthdays', 'clean-folder', 'edit-note',
                              'delete-note'])


class DefMain(ABC):
    
    @abstractmethod
    def main(self):
        pass


    
class ExitList(DefMain):
    def main(self):
        save()
        print(f'Good bye and have a nice day!')
        quit()



        
class WorkWithNotes(DefMain):
    
    def main(self):
        create_note()
        
    def show(self):
       show_notes()
       
    def find(self):
        find_tag()
        
    def edit(self):
        edit_note()
        
    def delete(self):
        delete_note()
        
        
        
    
        
       
class WorkWithFile(DefMain):
    
    def main(self):
        save()
        
    def load_data(self): 
        load()
        
    def find(self):
        find_record()
        
        
        
class WorkWithContacts(DefMain):
    
    def main(self):
        create_contact()
        
    def show(self):
        show_contacts()
        
    def delete(self):
        delete_contact()
        
        
        
class WorkWithPhone(DefMain):
    
    def main(self):
        add_phone()
        
    def edit(self):
        edit_phone()
        
    def find(self):
        find_phone()
        
    def remove(self):
        remove_phone()
        


class WorkWithEmail(DefMain):
    def main(self):
        add_email()
        
        
        
class WorkWithAddress(DefMain):
    def main(self):
        add_address()
            
            

class WorkWithBitrhday(DefMain):
    def main(self):
        add_birthday()
        
    def find(self):
        uncoming_birthdays()
        
    

class Helps(DefMain):
    
    def main(self):
        get_help()
        
    def clean(self):
        clean()
        
        
    



if __name__ == "__main__":
    
    boot_logo()
    load()
    
    exit_option = ExitList()
    notes_options = WorkWithNotes()
    file_options = WorkWithFile()
    contact_options = WorkWithContacts()
    phone_options = WorkWithPhone()
    email_options = WorkWithEmail()
    address_options = WorkWithAddress()
    birthday_options = WorkWithBitrhday()
    help_options = Helps()
    
    
    while True:
        operation = prompt('Bond says: ', completer=command_menu).lower()

        if operation.startswith(exit_list):
            exit_option.main()
        
        if operation.startswith('create-note'):
            notes_options.main()

        if operation.startswith('show-notes'):
            notes_options.show()

        if operation.startswith('find-tag'):
            notes_options.find()

        if operation.startswith('edit-note'):
            notes_options.edit()
            
        if operation.startswith('delete-note'):
            notes_options.delete()
            
        if operation.startswith('save-data'):
            file_options.main()
        
        if operation.startswith('load-data'):
            file_options.load_data()
            
        if operation.startswith('find-record'):
            file_options.find()

        if operation.startswith('create-contact'):
            contact_options.main()

        if operation.startswith('show-contacts'):
            contact_options.show()
        
        if operation.startswith('delete-contact'):
            contact_options.delete()

        if operation.startswith('add-phone'):
            phone_options.main()
            
        if operation.startswith('edit-phone'):
            phone_options.edit()

        if operation.startswith('find-phone'):
            phone_options.find()
        
        if operation.startswith('remove-phone'):
            phone_options.remove()
            
        if operation.startswith('add-email'):
            email_options.main()

        if operation.startswith('add-address'):
            address_options.main()

        if operation.startswith('add-birthday'):
            birthday_options.main()

        if operation.startswith('uncoming-birthdays'):
            birthday_options.find()
          
        if operation.startswith('clean-folder'):
            help_options.clean()
            
        if operation.startswith(help_comm):
            help_options.main()
        else:
            pass
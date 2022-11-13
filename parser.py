from telethon.sync import TelegramClient, events
import csv

api_id = '29146979'
api_hash = 'a787d0ec3dae7775bdd61b52bb753210'

client = TelegramClient('myNewSession', api_id, api_hash)

async def main():
    # Getting information about yourself
    me = await client.get_me()

    print('logged with:')
    print(f'username: {me.username}')
    print(f'phone number: {me.phone}')

    group_link = 'investtonmarket'  # Ссылка на чат, откуда будут доставаться пользователи
    _path = f'users_of_{group_link}_chat.csv'
    print(f'path: {_path} results') # Файл, куда будет выводиться результат парсинга

    with open(_path, 'w', encoding='cp1251', newline='') as file:  # Написание заголовков в .csv файл
        writer = csv.writer(file, delimiter=',')
        writer.writerow(
            (
                'user_name',
                'phone_number',
                'first_name',
                'second_name'
            )
        )

    
    participants = await client.get_participants(group_link)
    number_of_participants = 0
    with_numbers = 0

    for part in participants:

        try:
            user_name = part.to_dict()['username']
        except:
            user_name = ''

        try:
            phone_number = part.to_dict()['phone']
        except:
            phone_number = ''

        try:
            first_name = part.to_dict()['first_name']
        except:
            first_name = ''

        try:
            second_name = part.to_dict()['second_name']
        except:
            second_name = ''

        number_of_participants += 1

        if phone_number is not None:
            with_numbers += 1

        # Записываем результаты в .csv файл
        with open(_path, 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(
                (
                    user_name,
                    phone_number,
                    first_name,
                    second_name
                )
            )

    print(f'[INFO] | processed: {number_of_participants} users')
    print(f'[INFO] | with phone: {with_numbers} users')
                
        

with client:
    client.loop.run_until_complete(main())





    
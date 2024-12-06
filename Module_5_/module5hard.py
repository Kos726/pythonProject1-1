import time

t = "Hello, it's me!"

print(len(t), t[15])


class User:
	def __init__(self, nickname=None, password=None, age=0):
		self.nickname = nickname
		self.password = hash(password)
		self.age = age


class Video:
	def __init__(self, title=None, duration=0, time_now=0, adult_mode=False):
		self.title = title
		self.duration = duration
		self.time_now = time_now
		self.adult_mode = adult_mode
		

class UrTube(User, Video):
	def __init__(self):
		User.__init__(self)
		Video.__init__(self)
		self.users = []
		self.videos = []
		self.current_user = None
		
	def log_in(self, nickname, password):
		list_nicknames = [self.users[i].nickname for i in range(len(self.users))]
		list_passwords = [self.users[i].password for i in range(len(self.users))]
		dict_users = dict(zip(list_nicknames, list_passwords))
		_found = nickname in list_nicknames
		if _found is False:
			print(f'Пользователя с именем {nickname} не существует, пройдите регистрацию')
		elif _found is True:
			if hash(password) == dict_users[nickname]:
				self.current_user = nickname
				print(f'Рады приветствовать Вас {self.current_user}!')
		return self.current_user
		
	def register(self, nickname, password, age):
		list_nicknames = [self.users[i].nickname for i in range(len(self.users))]
		_found = nickname in list_nicknames
		if _found is True:
			print(f'Пользователь с именем {nickname} уже существует')
		elif _found is False:
			_new_user = User(nickname, password, age)
			self.users.append(_new_user)		
		return self.log_in(nickname, password)

	def log_out(self):
		self.current_user = None
		
	def add(self, *videos_new):
		list_titles = [self.videos[i].title for i in range(len(self.videos))]
		for i in range(len(videos_new)):
			_found = videos_new[i].title in list_titles
			if _found is False:
				self.videos.append(videos_new[i])
		return self.videos
		
	def get_videos(self, find_):
		_find = find_.lower()
		_array = self.videos
		_list_found = []
		for i in range(len(_array)):
			_found = _find in _array[i].title.lower()
			if _found is True:
				_list_found.append(_array[i].title)
		return f'{_list_found}'
		
	def watch_video(self, select_title):
		_array = self.videos
		if self.current_user is None:
			print('Войдите в аккаунт, чтобы смотреть видео')
		else:
			list_nicknames = [self.users[i].nickname for i in range(len(self.users))]
			list_age = [self.users[i].age for i in range(len(self.users))]
			dict_users = dict(zip(list_nicknames, list_age))
			if dict_users[self.current_user] >= 18:
				for i in range(len(_array)):
					_found = select_title in _array[i].title
					if _found is True:
						for sec_ in range(_array[i].duration):
							time.sleep(1)
							print(sec_ + 1)
						print('Конец видео')
			else:
				print('Извините, Вам нет 18 лет, видео недоступно')
		
		
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# v3 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# v4 = Video('Для чего програмисту компьютер?', 12)

# Добавление видео
ur.add(v1, v2)
# ur.add(v3, v4)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# u1 = User('vasya_pupkin', 'lolkekcheburek', 19)
# print(u1.nickname)

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.register('vasya_pupkin2', 'lolkekcheburek', 29)
# ur.register('vasya_pupkin', 'lolkekcheburek', 19)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

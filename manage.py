# 导入扩展flask-script扩展
from flask_script import Manager
# 导入扩展flask_migrate
from flask_migrate import Migrate, MigrateCommand
# 导入create_app函数
from flask_web import create_app, db

app = create_app('development')

# 实例化管理器对象
manage = Manager(app)
# 使用迁移框架
Migrate(app, db)
# 添加迁移命令
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # 打印路由映射
    # print(app.url_map)
    manage.run()

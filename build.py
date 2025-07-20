import os
import shutil
import random
from jinja2 import Environment, FileSystemLoader

# configuration
PUBLISH_TO_GITHUB_PAGES = False  # set to true to build for github pages
TEMPLATES_DIR = 'templates'
OUTPUT_DIR = 'dist'
STATIC_DIR = 'static'
# this should be your repository name
REPO_NAME = 'hswg'


def get_random_video():
    # assuming static folder is at the same level as templates
    video_dir = os.path.join(STATIC_DIR, 'content/videos')
    if os.path.exists(video_dir):
        video_files = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]
        if video_files:
            return random.choice(video_files)
    return None

def render_template(env, template_name, output_path, context):
    template = env.get_template(template_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template.render(context))

def main():
    # clean output directory
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    # setup jinja2 environment
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

    base_path = f'/{REPO_NAME}/' if PUBLISH_TO_GITHUB_PAGES else '/'

    # copy static files
    if os.path.exists(STATIC_DIR):
        shutil.copytree(STATIC_DIR, os.path.join(OUTPUT_DIR, 'static'))

    # render static pages
    pages_to_render = {
        'index.html': 'index.html',
        'repertoire.html': 'repertoire.html',
        'agenda.html': 'agenda.html',
        'about.html': 'about.html',
        'contact.html': 'contact.html',
    }

    for template_file, output_file in pages_to_render.items():
        context = {
            'video_filename': get_random_video(),
            'base_path': base_path
        }
        render_template(env, template_file, os.path.join(
            OUTPUT_DIR, output_file), context)
        print(f"rendered {output_file}")

    # generate wine pages
    wines = ["Johanniter", "Souvenir Gris", "Rondo", "Grappa"]
    for wine_name in wines:
        context = {
            'video_filename': get_random_video(),
            'base_path': base_path,
            'wine_name': wine_name
        }
        output_path = os.path.join(OUTPUT_DIR, 'repertoire', f'{wine_name.lower().replace(" ", "-")}.html')
        render_template(env, 'wine.html', output_path, context)
        print(f"rendered wine page for {wine_name}")


    # the /join route was pointing to contact.html, we can create a join.html that redirects or has the same content.
    # for simplicity, we'll make it a copy of contact.
    context = {
        'video_filename': get_random_video(),
        'base_path': base_path
    }
    render_template(env, 'contact.html', os.path.join(
        OUTPUT_DIR, 'join.html'), context)
    print("rendered join.html")

    print("static site generated in 'dist' folder.")

if __name__ == '__main__':
    main()

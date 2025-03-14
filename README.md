# Notes

Gabriel personal notes.
Created from [login-static-site](https://github.com/meadapt/login-static-site) repository.

## Usage

- Local server[^1]

```
git clone git@github.com:gabrielbdornas/notes.git
cd notes
poetry install
touch .env # Add GH_TOKEN to Document contributors plugin
task serve
```

- Commit and push changes are enoth to guild and deploy the content to render.
This push will trigger the `publish_render_pages` GitHub Actions workflow that builds the site and pushes the generated static files to the render-pages branch.

[^1]: See [Document contributors](https://squidfunk.github.io/mkdocs-material/setup/adding-a-git-repository/?h=document+contributors#document-contributors) documentation.

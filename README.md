# My own personal webpage!

# Development:

## Setup environment
### From Gemfile.lock
This installs all dependencies:
```
bundle install
```

### Fresh install:

Install appropriate ruby version and set it to be used in this project
```
rbenv install 3.3.12
rbenv local 3.3.12
```

Install jekyll and bundler
```
gem install bundler jekyll
```

## Serve
Serve the webpage locally:
```
bundler exec jekyll serve -o -l
```
Usefull options:
 - `--drafts` : render draft posts
 - `--future` : render future posts
 - `-o` : open browser
 - `-l` : live reload

To build page:
```
bundler exec jekyll build
```
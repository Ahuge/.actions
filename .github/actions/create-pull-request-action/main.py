import argparse
import os

from github import Github

TITLE = "Automatic Pull Request from {head} into {base}"
BODY = "Automatic Pull Request Body"
PULL_REQUEST_ID_KEY = "pull-request-id"
CREATED_KEY = "created"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("head")
    parser.add_argument("base")
    args = parser.parse_args()
    return args


def get_repo(github_instance, repository_name):
    for repo in github_instance.get_user().get_repos():
        if repo.name == repository_name:
            return repo


def main(head, base):
    e_token = os.environ.get("GITHUB_TOKEN")
    e_repository = os.environ.get("GITHUB_REPOSITORY")

    g = Github(e_token)
    repo = g.get_repo(e_repository)
    if not repo:
        message = "Could not load repository with name '{}'".format(e_repository)
        if not e_repository:
            message = "Could not load repository without having 'GITHUB_REPOSITORY' "\
                      "environment variable set"
        raise EnvironmentError(message)

    pull_requests = repo.get_pulls(state="open", sort="create", base=base, head=head)
    created = False
    if pull_requests.totalCount > 1:
        pull_request = pull_requests[0]
    elif pull_requests.totalCount == 0:
        pull_request = None
    else:
        pull_request = pull_requests[0]

    if pull_request is None:
        created = True
        print("Creating pull-request {base} <--- {head}".format(base=base, head=head))
        print(
            "title=%s" % TITLE.format(head=head, base=base),
            "body=%s" % BODY,
            "base=%s" % base,
            "head=%s" % head,
        )
        pull_request = repo.create_pull(
            title=TITLE.format(head=head, base=base),
            body=BODY,
            base=base,
            head=head,
        )

    return pull_request.id, created


def set_output(key, value):
    print("::set-output name={key}::{value}".format(
        key=key, value=value
    ))


if __name__ == "__main__":
   args = parse_args()
   pull_request_id, _created = main(head=args.head, base=args.base)
   set_output(PULL_REQUEST_ID_KEY, pull_request_id)
   set_output(CREATED_KEY, _created)

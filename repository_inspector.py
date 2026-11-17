def parse_repository_id(repository_id: str) -> tuple[str, str]:
    """Validate and split an owner/repo identifier."""
    stripped_id = repository_id.strip()
    if not stripped_id or '/' not in stripped_id:
        raise ValueError("Invalid repository identifier. Expected format: 'owner/repo'.")
   
    splitted = stripped_id.split('/')
    if len(splitted) == 2:
        owner, repo = splitted
        if len(owner) == 0 or len(repo) == 0:
            raise ValueError("Invalid repository identifier. Owner and repo cannot be empty.")
        return owner, repo
    else:
      
         raise ValueError("Invalid repository identifier. Expected format: 'owner/repo'.")

# Part 1 Questions

1. How woudl we filter for all books with titles containing the word 'Django'?

   `Book.objects.filter(title__name='Django')`

2. How wouldwe filter for all books with the tag 'Fiction'?

   `Book.objects.filter(tag__name='Fiction')`

3. How would we filter for all _authors_ who have _written_ books containing the word 'Django'?

   `Author.objects.filter(book__title='Django')`
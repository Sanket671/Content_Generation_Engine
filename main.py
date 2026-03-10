from trends_fetcher import get_trending_keywords
from trend_analyzer import analyze_trends
from blog_generator import generate_blog


def main():

    print("Fetching Google Trends data...")

    keywords = get_trending_keywords()

    print("\nTrending Keywords:")
    print(keywords)

    print("\nAnalyzing trends using AI...\n")

    analysis = analyze_trends(keywords)

    print(analysis)

    print("\nGenerating SEO Blog...\n")

    blog_path = generate_blog(keywords)

    print("Blog saved at:", blog_path)


if __name__ == "__main__":
    main()